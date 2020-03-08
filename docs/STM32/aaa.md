# Ssss

利用STM32串口中断收发和buffer机制（循环队列的原理）实现数据的准确接收和发送。为后续添加上层通信协议建立基础。为了方便使用，为函数接口统一标准

## Arduino串口机制的接口函数

```c
void begin(unsigned long baud);//初始化接口
void end(void);//关闭串口
int available(void);//获取缓存中可以读取的字节数
int peek(void);//从缓存中读取字节数据，但不删除该数据
int read(void);//从缓存中读取字节数据，并删除该数据
int availableWrite(void);//获取发送缓存还可以写入的字节数
void flush(void); //将发送缓存中的数据全部发送出去
void write(uint8_t c);//发送字节数据
```

## 代码实现

### 编写硬件层MSP支持代码

```c
void HAL_UART_MspInit(UART_HandleTypeDef* uartHandle)
{

  GPIO_InitTypeDef GPIO_InitStruct = {0};
  if(uartHandle->Instance==USART1)
  {
    /* USART1 clock enable */
    __HAL_RCC_USART1_CLK_ENABLE();
  
    __HAL_RCC_GPIOA_CLK_ENABLE();
    /**USART1 GPIO Configuration    
    PA9     ------> USART1_TX
    PA10     ------> USART1_RX 
    */
    GPIO_InitStruct.Pin = GPIO_PIN_9|GPIO_PIN_10;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_PULLUP;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_VERY_HIGH;
    GPIO_InitStruct.Alternate = GPIO_AF7_USART1;
    HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

    /* USART1 interrupt Init */
    HAL_NVIC_SetPriority(USART1_IRQn, 0, 0);
    HAL_NVIC_EnableIRQ(USART1_IRQn);
  }
}

void HAL_UART_MspDeInit(UART_HandleTypeDef* uartHandle)
{

  if(uartHandle->Instance==USART1)
  {
    /* Peripheral clock disable */
    __HAL_RCC_USART1_CLK_DISABLE();
  
    /**USART1 GPIO Configuration    
    PA9     ------> USART1_TX
    PA10     ------> USART1_RX 
    */
    HAL_GPIO_DeInit(GPIOA, GPIO_PIN_9|GPIO_PIN_10);

    /* USART1 interrupt Deinit */
    HAL_NVIC_DisableIRQ(USART1_IRQn);
  }
} 
```



### 定义新的串口结构体

```c
#define SERIAL_RX_BUFFER_SIZE  64
#define SERIAL_TX_BUFFER_SIZE  64
typedef struct
{
  UART_HandleTypeDef handle;
  IRQn_Type irq;
  uint8_t recv;
  uint8_t rx_buffer[SERIAL_RX_BUFFER_SIZE];
  uint8_t tx_buffer[SERIAL_TX_BUFFER_SIZE];
  uint16_t rx_head;
  volatile uint16_t rx_tail;
  volatile uint16_t tx_head;
  uint16_t tx_tail;
}Serial_t;
```



### 接口函数实现

#### 实例化对象

```c
Serial_t serial1;
//UART_HandleTypeDef *huart1 = &(serial1.handle);
Serial_t serial2; //实际未用到
```

#### `serial_init()`

```c
void serial_init(Serial_t *serial, uint32_t baud)
{
  UART_HandleTypeDef *huart = &(serial->handle);
  
  huart->Init.BaudRate = baud;
  huart->Init.WordLength = UART_WORDLENGTH_8B;
  huart->Init.StopBits = UART_STOPBITS_1;
  huart->Init.Parity = UART_PARITY_NONE;
  huart->Init.Mode = UART_MODE_TX_RX;
  huart->Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart->Init.OverSampling = UART_OVERSAMPLING_16;
  
  if(serial == &serial1)
  {
    huart->Instance = USART1;
    serial->irq = USART1_IRQn;
  }
  else if(serial == &serial2)
  {
    huart->Instance = USART2;
    serial->irq = USART2_IRQn;
  }
  if(HAL_UART_Init(huart) != HAL_OK)
  {
    Error_Handler();
  }
  //使能串口接收中断
  HAL_UART_Receive_IT(huart, &(serial->recv), 1);
}

```

#### `serial_available()`

```c
int serial_available(Serial_t *serial)
{
  return (uint32_t)(SERIAL_RX_BUFFER_SIZE + serial->rx_head - serial->rx_tail) % SERIAL_RX_BUFFER_SIZE;
}
```

#### `serial_peek()`

```c
int serial_peek(Serial_t *serial)
{
  if(serial->rx_head == serial->rx_tail)
  {
    return -1;
  }
  else
  {
    return serial->rx_buffer[serial->rx_tail];
  } 
}
```

#### `serial_read()`

```c
int serial_read(Serial_t *serial)
{
  if(serial->rx_head == serial->rx_tail)
  {
    return -1;
  }
  else
  {
    uint8_t c = serial->rx_buffer[serial->rx_tail];
    serial->rx_tail = (uint16_t)(serial->rx_tail + 1) % SERIAL_RX_BUFFER_SIZE;
    return c;
  }
}
```

#### `availableWrite()`

```c
int serial_availableForWrite(Serial_t *serial)
{
  return (uint32_t)(SERIAL_TX_BUFFER_SIZE + serial->tx_tail - serial->tx_head - 1) % SERIAL_TX_BUFFER_SIZE;
}
```

#### `serial_flush`

```c
//只有在执行过serial_write()函数后才可使用该函数。
void serial_flush(Serial_t *serial)
{
  while ((serial->tx_head != serial->tx_tail)) {
    // nop, the interrupt handler will free up space for us
  }
  // If we get here, nothing is queued anymore (DRIE is disabled) and
  // the hardware finished tranmission (TXC is set).
}
```

#### `serial_write()`

```c
void serial_write(Serial_t *serial, uint8_t c)
{
  //HAL_UART_Transmit(&(serial->handle),&c,1,1000);
  uint16_t i = (serial->tx_head + 1) % SERIAL_TX_BUFFER_SIZE;
  
  while(i == serial->tx_tail)  //发送缓冲区满
  {
    //什么也不做，等待缓冲区有空间
  }
  
  serial->tx_buffer[serial->tx_head] = c;
  serial->tx_head = i;
  
  if((HAL_UART_GetState(&(serial->handle)) & HAL_UART_STATE_BUSY_TX) != HAL_UART_STATE_BUSY_TX)
  {
    /* Must disable interrupt to prevent handle lock contention */
    HAL_NVIC_DisableIRQ(serial->irq);
    HAL_UART_Transmit_IT(&(serial->handle), &(serial->tx_buffer[serial->tx_tail]), 1);
    HAL_NVIC_EnableIRQ(serial->irq);
  }
}

```



### 中断服务函数

#### 接收中断回调函数

```c
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
  if(huart == &(serial1.handle))
  {
    uint16_t i = (uint32_t)(serial1.rx_head +1) % SERIAL_RX_BUFFER_SIZE;
    
    if(i != serial1.rx_tail)
    {
      serial1.rx_buffer[serial1.rx_head] = serial1.recv;
      serial1.rx_head = i;
    }
    /* 使能下次接收中断 */
    HAL_UART_Receive_IT(huart, &(serial1.recv), 1);
  }
}
```



#### 发送中断回调函数

```c
void HAL_UART_TxCpltCallback(UART_HandleTypeDef *huart)
{
  if(huart == &(serial1.handle))
  {
    serial1.tx_tail = (serial1.tx_tail + 1) % SERIAL_TX_BUFFER_SIZE;
    if(serial1.tx_head == serial1.tx_tail)
    {
      return;
    }
    /* 发送完成后，再次使能中断发送直至发送缓冲区的数据全部发送完成 */
    if (HAL_UART_Transmit_IT(huart, &serial1.tx_buffer[serial1.tx_tail], 1) != HAL_OK) {
      return;
    }
  }
}
```



#### 中断函数

```c
/**
  * @brief This function handles USART1 global interrupt.
  */
void USART1_IRQHandler(void)
{
  HAL_UART_IRQHandler(&(serial1.handle));
}
```

### 测试

```c
int main(void)
{
    /* 省略了初始化函数 */
    while(1)
    {
    	if(serial_available(&serial1))
    	{
        	uint8_t c = serial_read(&serial1);
        	serial_write(&serial1,c)
    	}    
    }    
}
```

利用该测试函数可以实现串口的回环接收。