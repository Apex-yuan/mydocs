# Arduino_Core_STM32---pinMode()实现分析

## pinMode()定义

Arduino平台的易于使用性主要就体现在屏蔽的大量底层细节的实现，对于该函数来说也不例外。虽然该函数只有两个参数（arduino引脚号和模式），但这两个参数需要多层的映射才能转化为具体适合STM32芯片的配置信息，并调用底层接口完成配置。

从下面源码中可以看出主要由两个函数来完成引脚模式配置的：`digitalPinToPinName()`和`pinfunction()`。在具体深入下面两个函数之前我们需要一些预备知识---该库对于STM32硬件端口和引脚的封装。

```c
void pinMode(uint32_t ulPin, uint32_t ulMode)
{
  PinName p = digitalPinToPinName(ulPin);

  if (p != NC) {
    // If the pin that support PWM or DAC output, we need to turn it off
	/* 省略关闭PWM或DAC输出的代码 */
    switch (ulMode) {
      case INPUT: /* INPUT_FLOATING */
        pin_function(p, STM_PIN_DATA(STM_MODE_INPUT, GPIO_NOPULL, 0));
        break;
      case INPUT_PULLUP:
        pin_function(p, STM_PIN_DATA(STM_MODE_INPUT, GPIO_PULLUP, 0));
        break;
      case INPUT_PULLDOWN:
        pin_function(p, STM_PIN_DATA(STM_MODE_INPUT, GPIO_PULLDOWN, 0));
        break;
      case INPUT_ANALOG:
        pin_function(p, STM_PIN_DATA(STM_MODE_ANALOG, GPIO_NOPULL, 0));
        break;
      case OUTPUT:
        pin_function(p, STM_PIN_DATA(STM_MODE_OUTPUT_PP, GPIO_NOPULL, 0));
        break;
      case OUTPUT_OPEN_DRAIN:
        pin_function(p, STM_PIN_DATA(STM_MODE_OUTPUT_OD, GPIO_NOPULL, 0));
        break;
      default:
        Error_Handler();
        break;
    }
  }
}
```

## 预备知识

### `PortNames.c/h`文件解析

定义端口枚举：

```c
typedef enum {
  FirstPort = 0x00,
  PortA = FirstPort,
  PortB,
#if defined GPIOC_BASE
  PortC,
#endif
#if defined GPIOD_BASE
  PortD,
#endif
/* 省略部分定义 */
  PortZ,
  LastPort = PortZ - 1
} PortName;

#define MAX_NB_PORT (LastPort-FirstPort+1)

```

定义GPIO端口表

```c
GPIO_TypeDef *GPIOPort[MAX_NB_PORT] = {
  (GPIO_TypeDef *)GPIOA_BASE,
  (GPIO_TypeDef *)GPIOB_BASE
#if defined GPIOC_BASE
  , (GPIO_TypeDef *)GPIOC_BASE
#endif
#if defined GPIOD_BASE
  , (GPIO_TypeDef *)GPIOD_BASE
#endif
/* 省略部分代码 */
};
```

操作函数：返回GPIO基地址

```c
/* Return GPIO base address */
#define get_GPIO_Port(p) ((p < MAX_NB_PORT) ? GPIOPort[p] : (GPIO_TypeDef *)NULL)
```



### `pinNames.h`文件解析

引脚定义：实际引脚定义中也包含的端口信息，**高四位存储端口信息（PortName的枚举值），低四位存储引脚号（0-15）**。

```c
typedef enum {
  // Not connected
  NC = (int)0xFFFFFFFF,

  // Pin name definition
  PA_0  = (PortA << 4) + 0x00,
  PA_1  = (PortA << 4) + 0x01,
  PA_2  = (PortA << 4) + 0x02,
  PA_3  = (PortA << 4) + 0x03,
  PA_4  = (PortA << 4) + 0x04,
  PA_5  = (PortA << 4) + 0x05,
  PA_6  = (PortA << 4) + 0x06,
  PA_7  = (PortA << 4) + 0x07,
  PA_8  = (PortA << 4) + 0x08,
  PA_9  = (PortA << 4) + 0x09,
  PA_10 = (PortA << 4) + 0x0A,
  PA_11 = (PortA << 4) + 0x0B,
  PA_12 = (PortA << 4) + 0x0C,
  PA_13 = (PortA << 4) + 0x0D,
  PA_14 = (PortA << 4) + 0x0E,
  PA_15 = (PortA << 4) + 0x0F,

  PB_0  = (PortB << 4) + 0x00,
  PB_1  = (PortB << 4) + 0x01,
  PB_2  = (PortB << 4) + 0x02,
  PB_3  = (PortB << 4) + 0x03,
  PB_4  = (PortB << 4) + 0x04,
  PB_5  = (PortB << 4) + 0x05,
  PB_6  = (PortB << 4) + 0x06,
  PB_7  = (PortB << 4) + 0x07,
  PB_8  = (PortB << 4) + 0x08,
  PB_9  = (PortB << 4) + 0x09,
  PB_10 = (PortB << 4) + 0x0A,
  PB_11 = (PortB << 4) + 0x0B,
  PB_12 = (PortB << 4) + 0x0C,
  PB_13 = (PortB << 4) + 0x0D,
  PB_14 = (PortB << 4) + 0x0E,
  PB_15 = (PortB << 4) + 0x0F,
#if defined GPIOC_BASE
  /* 省略GPIOC的引脚定义 */
#endif
  /* 省略GPIOD-GPIOJ之间的引脚定义 */
  // Specific pin name
  PADC_BASE = 0x100,
  /* 省略部分特殊引脚的定义 */
  // Specific pin name define in the variant
#if __has_include("PinNamesVar.h")
#include "PinNamesVar.h"
#endif
  P_END = NC
} PinName;
```

### `PinNamesTypes.h`文件解析

使用在pin_function函数中的STM引脚数据，按如下32位格式的编码：

- [2:0] Function (like in MODER reg) : Input / Output / Alt / Analog

- [3] Output Push-Pull / Open Drain (as in OTYPER reg)

- [5:4] as in PUPDR reg: No Pull, Pull-up, Pull-Down

- [7:6] Reserved for speed config (as in OSPEEDR), but not used yet

- [14:8] Alternate Num (as in AFRL/AFRG reg)

- [19:15] Channel (Analog/Timer specific)

- [20] Inverted (Analog/Timer specific)

- [21] Analog ADC control - Only valid for specific families

- [32:22] Reserved

编码信息的细节定义

```c
#define STM_PIN_FUNCTION_MASK 0x07
#define STM_PIN_FUNCTION_SHIFT 0
#define STM_PIN_FUNCTION_BITS (STM_PIN_FUNCTION_MASK << STM_PIN_FUNCTION_SHIFT)

#define STM_PIN_OD_MASK 0x01
#define STM_PIN_OD_SHIFT 3
#define STM_PIN_OD_BITS (STM_PIN_OD_MASK << STM_PIN_OD_SHIFT)

#define STM_PIN_PUPD_MASK 0x03
#define STM_PIN_PUPD_SHIFT 4
#define STM_PIN_PUPD_BITS (STM_PIN_PUPD_MASK << STM_PIN_PUPD_SHIFT)

#define STM_PIN_SPEED_MASK 0x03
#define STM_PIN_SPEED_SHIFT 6
#define STM_PIN_SPEED_BITS (STM_PIN_SPEED_MASK << STM_PIN_SPEED_SHIFT)

#define STM_PIN_AFNUM_MASK 0x7F
#define STM_PIN_AFNUM_SHIFT 8
#define STM_PIN_AFNUM_BITS (STM_PIN_AFNUM_MASK << STM_PIN_AFNUM_SHIFT)

#define STM_PIN_CHAN_MASK 0x1F
#define STM_PIN_CHAN_SHIFT 15
#define STM_PIN_CHANNEL_BIT (STM_PIN_CHAN_MASK << STM_PIN_CHAN_SHIFT)

#define STM_PIN_INV_MASK 0x01
#define STM_PIN_INV_SHIFT 20
#define STM_PIN_INV_BIT (STM_PIN_INV_MASK << STM_PIN_INV_SHIFT)

#define STM_PIN_AN_CTRL_MASK 0x01
#define STM_PIN_AN_CTRL_SHIFT 21
#define STM_PIN_ANALOG_CONTROL_BIT (STM_PIN_AN_CTRL_MASK << STM_PIN_AN_CTRL_SHIFT)

```

方便从数据编码中解析出具体配置的宏函数：

```c
#define STM_PIN_FUNCTION(X)         (((X) >> STM_PIN_FUNCTION_SHIFT) & STM_PIN_FUNCTION_MASK)
#define STM_PIN_OD(X)               (((X) >> STM_PIN_OD_SHIFT) & STM_PIN_OD_MASK)
#define STM_PIN_PUPD(X)             (((X) >> STM_PIN_PUPD_SHIFT) & STM_PIN_PUPD_MASK)
#define STM_PIN_SPEED(X)            (((X) >> STM_PIN_SPEED_SHIFT) & STM_PIN_SPEED_MASK)
#define STM_PIN_AFNUM(X)            (((X) >> STM_PIN_AFNUM_SHIFT) & STM_PIN_AFNUM_MASK)
#define STM_PIN_CHANNEL(X)          (((X) >> STM_PIN_CHAN_SHIFT) & STM_PIN_CHAN_MASK)
#define STM_PIN_INVERTED(X)         (((X) >> STM_PIN_INV_SHIFT) & STM_PIN_INV_MASK)
#define STM_PIN_ANALOG_CONTROL(X)   (((X) >> STM_PIN_AN_CTRL_SHIFT) & STM_PIN_AN_CTRL_MASK)
#define STM_PIN_MODE(X)             ((STM_PIN_OD((X)) << 4) | \
                                      (STM_PIN_FUNCTION((X)) & (~STM_PIN_OD_BITS)))

#define STM_PIN_DEFINE(FUNC_OD, PUPD, AFNUM)  ((int)(FUNC_OD) |\
                          ((PUPD  & STM_PIN_PUPD_MASK) << STM_PIN_PUPD_SHIFT) |\
                          ((AFNUM & STM_PIN_AFNUM_MASK) << STM_PIN_AFNUM_SHIFT))

#define STM_PIN_DEFINE_EXT(FUNC_OD, PUPD, AFNUM, CHAN, INV) \
                                            ((int)(FUNC_OD) |\
                       ((PUPD   & STM_PIN_PUPD_MASK) << STM_PIN_PUPD_SHIFT) |\
                       ((AFNUM  & STM_PIN_AFNUM_MASK) << STM_PIN_AFNUM_SHIFT) |\
                       ((CHAN   & STM_PIN_CHAN_MASK) << STM_PIN_CHAN_SHIFT) |\
                       ((INV    & STM_PIN_INV_MASK) << STM_PIN_INV_SHIFT))


```

为方便外部使用定义的宏：

```c
/*
 * MACROS to support the legacy definition of PIN formats
 * The STM_MODE_ defines contain the function and the Push-pull/OpenDrain
 * configuration (legacy inheritance).
 */
#define STM_PIN_DATA(FUNC_OD, PUPD, AFNUM) \
            STM_PIN_DEFINE(FUNC_OD, PUPD, AFNUM)
#define STM_PIN_DATA_EXT(FUNC_OD, PUPD, AFNUM, CHANNEL, INVERTED) \
            STM_PIN_DEFINE_EXT(FUNC_OD, PUPD, AFNUM, CHANNEL, INVERTED)

typedef enum {
  STM_PIN_INPUT = 0,
  STM_PIN_OUTPUT = 1,
  STM_PIN_ALTERNATE = 2,
  STM_PIN_ANALOG = 3,
} StmPinFunction;

#define STM_MODE_INPUT               (STM_PIN_INPUT)
#define STM_MODE_OUTPUT_PP           (STM_PIN_OUTPUT)
#define STM_MODE_OUTPUT_OD           (STM_PIN_OUTPUT | STM_PIN_OD_BITS)
#define STM_MODE_AF_PP               (STM_PIN_ALTERNATE)
#define STM_MODE_AF_OD               (STM_PIN_ALTERNATE | STM_PIN_OD_BITS)
#define STM_MODE_ANALOG              (STM_PIN_ANALOG)
#define STM_MODE_ANALOG_ADC_CONTROL  (STM_PIN_ANALOG | STM_PIN_ANALOG_CONTROL_BIT)
```

## `digitalPinToPinName()`函数

这里我们要搞清楚几个关于引脚的概念：Arduino引脚，PinName，STM32端口和引脚。

- Arduino引脚：数字编号（0-10...）或重新定义的宏（PA1，PA2...）
- PinName：封装了STM32的端口和引脚信息
- STM32端口和引脚：具体的STM32芯片的端口（GPIOx）和引脚（GPIO_PIN_x）

宏函数：通过查表将Arduino引脚号转化为对STM32端口和引脚编码的PinName。

```c
// Convert a digital pin number Dxx to a PinName PX_n
// Note: Analog pin is also a digital pin.
#define digitalPinToPinName(p)      (((uint32_t)p < NUM_DIGITAL_PINS) ? digitalPin[p] : NC)
```

通过下面数组可以将Arduino（Dx或x）引脚号转化为STM32的PinName（PX_n），下面具体是black_STM32F407VE板子的引脚定义（位于`variants.h`文件）

```c
// Pin number
// This array allows to wrap Arduino pin number(Dx or x)
// to STM32 PinName (PX_n)
const PinName digitalPin[] = {
  // Right Side
  //Int   //Ext
  //3V3   //3V3
  //3V3   //3V3
  //BOOT0 //BOOT1
  //GND   //GND
  //GND   //GND
  PE_1,   PE_0,   // D0, D1
  PB_9,   PB_8,
  PB_7,   PB_6,
  PB_5,   PB_3,
  PD_7,   PD_6,
  PD_5,   PD_4,   // D10, D11
  PD_3,   PD_2,
  PD_1,   PD_0,
  PC_12,  PC_11,
  PC_10,  PA_15,
  PA_12,  PA_11,  // D20, D21 PA_11: USB_DM, PA_12: USB_DP
  PA_10,  PA_9,
  PA_8,   PC_9,
  PC_8,   PC_7,
  PC_6,   PD_15,
  PD_14,  PD_13,  // D30, D31
  PD_12,  PD_11,
  PD_10,  PD_9,
  PD_8,   PB_15,
  // Left Side
  //Ext   //Int
  //5V    //5V
  //5V    //5V
  //3V3   //3V3
  //3V3   //3V3
  //GND   //GND
  PE_2,   PE_3,
  PE_4,   PE_5,   // D40, D41 PE_4: BUT K0, PE_5: BUT K1
  PE_6,   PC_13,
  PC_0,   PC_1,
  PC_2,   PC_3,
  //VREF- //VREF+
  PA_0,   PA_1,   // PA_0(WK_UP): BUT K_UP)
  PA_2,   PA_3,   // D50, D51
  PA_4,   PA_5,
  /*PA_6,   PA_7,*/ // PA_6, PA_7: Moved to allow contiguous analog pins
  PC_4,   PC_5,
  PB_0,   PB_1,
  PA_6,   PA_7,   // PA_6: LED D2, PA_7: LED D3 (active LOW)
  PE_7,   PE_8,   // D60, D61
  PE_9,   PE_10,
  PE_11,  PE_12,
  PE_13,  PE_14,
  PE_15,  PB_10,
  PB_11,  PB_12,  // D70, D71
  PB_13,  PB_14,
  PB_4,
};
```



## `pin_function()`函数

最终的配置是由该函数解析配置信息并调用底层库(LL库)函数实现的。

```c
/**
 * Configure pin (mode, speed, output type and pull-up/pull-down)
 */
void pin_function(PinName pin, int function)
{
  /* Get the pin informations */
  uint32_t mode  = STM_PIN_FUNCTION(function);
  uint32_t afnum = STM_PIN_AFNUM(function);
  uint32_t port = STM_PORT(pin);
  uint32_t ll_pin  = STM_LL_GPIO_PIN(pin);
  uint32_t ll_mode = 0;

  if (pin == (PinName)NC) {
    Error_Handler();
  }

  /* Enable GPIO clock */
  GPIO_TypeDef *gpio = set_GPIO_Port_Clock(port);

  /*  Set default speed to high.
   *  For most families there are dedicated registers so it is
   *  not so important, register can be set at any time.
   *  But for families like F1, speed only applies to output.
   */
#if defined (STM32F1xx)
  if (mode == STM_PIN_OUTPUT) {
#endif
#ifdef LL_GPIO_SPEED_FREQ_VERY_HIGH
    LL_GPIO_SetPinSpeed(gpio, ll_pin, LL_GPIO_SPEED_FREQ_VERY_HIGH);
#else
    LL_GPIO_SetPinSpeed(gpio, ll_pin, LL_GPIO_SPEED_FREQ_HIGH);
#endif
#if defined (STM32F1xx)
  }
#endif

  switch (mode) {
    case STM_PIN_INPUT:
      ll_mode = LL_GPIO_MODE_INPUT;
      break;
    case STM_PIN_OUTPUT:
      ll_mode = LL_GPIO_MODE_OUTPUT;
      break;
    case STM_PIN_ALTERNATE:
      ll_mode = LL_GPIO_MODE_ALTERNATE;
      /* In case of ALT function, also set the afnum */
      pin_SetAFPin(gpio, pin, afnum);
      break;
    case STM_PIN_ANALOG:
      ll_mode = LL_GPIO_MODE_ANALOG;
      break;
    default:
      Error_Handler();
      break;
  }
  LL_GPIO_SetPinMode(gpio, ll_pin, ll_mode);

  /* 省略部分代码 */

  if ((mode == STM_PIN_OUTPUT) || (mode == STM_PIN_ALTERNATE)) {
    if (STM_PIN_OD(function)) {
      LL_GPIO_SetPinOutputType(gpio, ll_pin, LL_GPIO_OUTPUT_OPENDRAIN);
    } else {
      LL_GPIO_SetPinOutputType(gpio, ll_pin, LL_GPIO_OUTPUT_PUSHPULL);
    }
  }

  pin_PullConfig(gpio, ll_pin, STM_PIN_PUPD(function));

  pin_DisconnectDebug(pin);
}
```



