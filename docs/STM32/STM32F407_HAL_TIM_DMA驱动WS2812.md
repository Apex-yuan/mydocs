# STM32F407_HAL_TIM_DMA驱动WS2812

初始化函数可以通过CubeMX配置，这里直接通过原码记录：

## 芯片外设层驱动

- `tim.h`

```c
#ifndef __TIM_H
#define __TIM_H

#include "stm32f4xx.h"

extern TIM_HandleTypeDef htim3;

void HAL_TIM_MspPostInit(TIM_HandleTypeDef* timHandle);
void tim3_init(void);

#endif /* __TIM_H */


```

- `tim.c`

```c
#include "tim.h"

TIM_HandleTypeDef htim3;
DMA_HandleTypeDef hdma_tim3_ch1_trig;

void tim3_init(void)
{
  TIM_MasterConfigTypeDef sMasterConfig;
  TIM_OC_InitTypeDef sConfigOC;

  htim3.Instance = TIM3;
  htim3.Init.Prescaler = 0;
  htim3.Init.CounterMode = TIM_COUNTERMODE_UP;
  htim3.Init.Period = 105-1;
  htim3.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  if (HAL_TIM_PWM_Init(&htim3) != HAL_OK)
  {
    // _Error_Handler(__FILE__, __LINE__);
  }

  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim3, &sMasterConfig) != HAL_OK)
  {
    // _Error_Handler(__FILE__, __LINE__);
  }

  sConfigOC.OCMode = TIM_OCMODE_PWM1;
  sConfigOC.Pulse = 0;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
  sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
  if (HAL_TIM_PWM_ConfigChannel(&htim3, &sConfigOC, TIM_CHANNEL_1) != HAL_OK)
  {
    // _Error_Handler(__FILE__, __LINE__);
  }

  HAL_TIM_MspPostInit(&htim3);
}

void HAL_TIM_PWM_MspInit(TIM_HandleTypeDef* tim_pwmHandle)
{

  if(tim_pwmHandle->Instance==TIM3)
  {
    /* TIM3 clock enable */
    __HAL_RCC_TIM3_CLK_ENABLE();
    /* DMA controller clock enable */
    __HAL_RCC_DMA1_CLK_ENABLE();
  
    /* TIM3 DMA Init */
    /* TIM3_CH1_TRIG Init */
    hdma_tim3_ch1_trig.Instance = DMA1_Stream4;
    hdma_tim3_ch1_trig.Init.Channel = DMA_CHANNEL_5;
    hdma_tim3_ch1_trig.Init.Direction = DMA_MEMORY_TO_PERIPH;
    hdma_tim3_ch1_trig.Init.PeriphInc = DMA_PINC_DISABLE;
    hdma_tim3_ch1_trig.Init.MemInc = DMA_MINC_ENABLE;
    hdma_tim3_ch1_trig.Init.PeriphDataAlignment = DMA_PDATAALIGN_HALFWORD;
    hdma_tim3_ch1_trig.Init.MemDataAlignment = DMA_MDATAALIGN_HALFWORD;
    hdma_tim3_ch1_trig.Init.Mode = DMA_NORMAL;
    hdma_tim3_ch1_trig.Init.Priority = DMA_PRIORITY_MEDIUM;
    hdma_tim3_ch1_trig.Init.FIFOMode = DMA_FIFOMODE_DISABLE;
    if (HAL_DMA_Init(&hdma_tim3_ch1_trig) != HAL_OK)
    {
      // _Error_Handler(__FILE__, __LINE__);
    }

    /* Several peripheral DMA handle pointers point to the same DMA handle.
     Be aware that there is only one stream to perform all the requested DMAs. */
    __HAL_LINKDMA(tim_pwmHandle,hdma[TIM_DMA_ID_CC1],hdma_tim3_ch1_trig);
    __HAL_LINKDMA(tim_pwmHandle,hdma[TIM_DMA_ID_TRIGGER],hdma_tim3_ch1_trig);

    /* TIM3 interrupt Init */
    HAL_NVIC_SetPriority(TIM3_IRQn, 0, 0);
    HAL_NVIC_EnableIRQ(TIM3_IRQn);
    
    /* DMA interrupt init */
    /* DMA1_Stream4_IRQn interrupt configuration */
    HAL_NVIC_SetPriority(DMA1_Stream4_IRQn, 0, 0);
    HAL_NVIC_EnableIRQ(DMA1_Stream4_IRQn);

  }
}

void HAL_TIM_MspPostInit(TIM_HandleTypeDef* timHandle)
{
  GPIO_InitTypeDef GPIO_InitStruct;
  if(timHandle->Instance==TIM3)
  {
    /* GPIOA clock enable */
    __HAL_RCC_GPIOA_CLK_ENABLE();
  
    /**TIM3 GPIO Configuration    
    PA6     ------> TIM3_CH1 
    */
    GPIO_InitStruct.Pin = GPIO_PIN_6;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF2_TIM3;
    HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);
  }
}

void HAL_TIM_PWM_MspDeInit(TIM_HandleTypeDef* tim_pwmHandle)
{
  if(tim_pwmHandle->Instance==TIM3)
  {
    /* Peripheral clock disable */
    __HAL_RCC_TIM3_CLK_DISABLE();

    /* TIM3 DMA DeInit */
    HAL_DMA_DeInit(tim_pwmHandle->hdma[TIM_DMA_ID_CC1]);
    HAL_DMA_DeInit(tim_pwmHandle->hdma[TIM_DMA_ID_TRIGGER]);

    /* TIM3 interrupt Deinit */
    HAL_NVIC_DisableIRQ(TIM3_IRQn);
  }
} 


/**
* @brief This function handles DMA1 stream4 global interrupt.
*/
void DMA1_Stream4_IRQHandler(void)
{
  HAL_DMA_IRQHandler(&hdma_tim3_ch1_trig);
}

/**
* @brief This function handles TIM3 global interrupt.
*/
void TIM3_IRQHandler(void)
{
  HAL_TIM_IRQHandler(&htim3);
}
```

## WS2812硬件驱动

- `ws281x.h`

```c
#ifndef __WS281X_H
#define __WS281x_H

#include "tim.h"

void ws281x_init(void);
void ws281x_show(void);
uint32_t ws281x_color(uint8_t r, uint8_t g, uint8_t b);
void ws281x_setColor(uint16_t n, uint32_t color);
void ws281x_close(void);

#endif /* __WS281X_H */


```

- `ws281x.c`

```c
#include "WS281x.h"
#include <string.h>

#ifndef PIXEL_NUM
  #define PIXEL_NUM 5
#endif
#define GRB (3*8)

#define WS_TERO 30
#define WS_ONE  45

/* pwm 占空比数值为uint16_t 类型，DMA传输时只能以半字输出，pixelBuffer应为uint16_t 类型 */
uint16_t pixelBuffer[PIXEL_NUM][GRB]; 

void ws281x_init(void)
{
  /* 配置TIM3 pwm频率为800Khz */
  tim3_init();
}

void ws281x_show(void)
{
  HAL_TIM_PWM_Start_DMA(&htim3, TIM_CHANNEL_1, (uint32_t *)pixelBuffer, PIXEL_NUM * GRB);
}

uint32_t ws281x_color(uint8_t r, uint8_t g, uint8_t b)
{
  return (uint32_t)(g << 16 | r << 8 | b);
}

/* pixel num from 0 start */
void ws281x_setColor(uint16_t n, uint32_t color)
{
  if(n < PIXEL_NUM)
  {
    for(uint8_t i = 0; i < GRB; ++i)
    {
      pixelBuffer[n][i] = ((color << i) & 0x800000) ? WS_ONE : WS_TERO;
    }
  }
}

void ws281x_close(void)
{
  uint16_t* ptr = (uint16_t *)pixelBuffer; 
  for(uint16_t i = 0; i < PIXEL_NUM * GRB; ++i)
  {
    *ptr++ = WS_TERO;
  }
  ws281x_show();
}

/* 中断回调函数，在设定的pwm通过DMA发送完成后会调用 */
void HAL_TIM_PWM_PulseFinishedCallback(TIM_HandleTypeDef* htim)
{
  __HAL_TIM_SetCompare(htim, TIM_CHANNEL_1, 0); //占空比清0，若不清会导致灯珠颜色不对 
  HAL_TIM_PWM_Stop_DMA(htim, TIM_CHANNEL_1);
}
```

## 结语

这里只实现了底层驱动接口，未移植显示效果部分的代码，显示效果可参考我的其他WS2812相关文章。HAL库分层效果确实好，但内部代码的理解难度要高很多，边用边学，加油！