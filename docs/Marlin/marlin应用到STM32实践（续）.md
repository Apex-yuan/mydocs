---
typora-root-url: ./
---

在上篇内容中主要介绍了marlin2.0安装到已有开发板的实例。这篇内容将通过marlin2.0安装到BLACK_STM32F407VE开发板的实践介绍如何为新定制的开发板烧入固件并详细介绍前期的处理过程，希望能为那些想深入固件研究苦于不会编译安装和想绘制3D打印机开发板又不知如何烧录固件的marlin爱好者一些帮助。

BLACK_STM32F407VE开发板的硬件开源资料链接：[https://github.com/mcauser/BLACK_F407VE](https://github.com/mcauser/BLACK_F407VE)

## 构建过程

类似于上篇文章的内容，首先将配置内容修改为适合于BLACK_STM32F407VE的开发板。

1. 将`platformio.ini`文件中的`[plarformio]`下的`default_envs`修改为

   ```python
   default_envs = STM32F407VE_black
   ```

2. 将`configuration.h`文件中的`MOTHERBOARD`修改为：

   ```c++
   #ifndef MOTHERBOARD
     #define MOTHERBOARD BOARD_BLACK_STM32F407VE
   #endif
   ```

3. 将`configuration.h`文件中的串口1`SERIAL_PORT`修改为`-1`或`1`

   ```c
   #define SERIAL_PORT -1  //USB虚拟串口
   ```

   `SERIAL_PORT`定义为`-1`是选择USB端口作为虚拟串口使用（可能需要STM32的虚拟串口驱动）。

   ```c
   #define SERIAL_PORT 1  //普通串口1
   ```

   `SERIAL_PORT`定义为`1`是选择开发板的串口1作为通信端口，当然也可以定义为2，3，4等，此时选择的便是串口2、串口3、串口4等串口。

   -----

   **`Note`**

   对于串口端口2`SERIAL_PORT_2`的注释不要去除，保持原样，在需要一定的配置后才能使用串口端口2，否则会编译出错（当然如果串口端口1使用串口1/USB虚拟串口，串口端口2使用USB虚拟串口/串口1的情况下不需要额外配置，若要使用其它串口则需要配置）。后面我们会说到如何使用它。

   ```c
   //#define SERIAL_PORT_2 -1
   ```

   -----

正常情况下通过以上3步的过程，就能够编译通过了，也可以下载到开发板中体验一番了。

## 构建分析

1. `platformio.ini`文件在将`default_envs`配置为`STM32F407VE_black`之后实际起作用的就是下文中的这些内容：

   ```ini
   [platformio]
   src_dir      = Marlin
   boards_dir   = buildroot/share/PlatformIO/boards
   default_envs = STM32F407VE_black
   
   [common]
   default_src_filter = +<src/*> -<src/config> -<src/HAL> +<src/HAL/shared>
   extra_scripts = pre:buildroot/share/PlatformIO/scripts/common-cxxflags.py
   build_flags = -fmax-errors=5 -g -D__MARLIN_FIRMWARE__ -fmerge-all-constants
   lib_deps =
     LiquidCrystal
     TMCStepper@>=0.6.2,<1.0.0
     Adafruit NeoPixel
     U8glib-HAL=https://github.com/MarlinFirmware/U8glib-HAL/archive/bugfix.zip
     Adafruit_MAX31865=https://github.com/adafruit/Adafruit_MAX31865/archive/master.zip
     LiquidTWI2=https://github.com/lincomatic/LiquidTWI2/archive/master.zip
     Arduino-L6470=https://github.com/ameyer/Arduino-L6470/archive/0.8.0.zip
     SailfishLCD=https://github.com/mikeshub/SailfishLCD/archive/master.zip
     SailfishRGB_LED=https://github.com/mikeshub/SailfishRGB_LED/archive/master.zip
     SlowSoftI2CMaster=https://github.com/mikeshub/SlowSoftI2CMaster/archive/master.zip
     
   #
   # STM32F407VET6 with RAMPS-like shield
   # 'Black' STM32F407VET6 board - http://wiki.stm32duino.com/index.php?title=STM32F407
   # Shield - https://github.com/jmz52/Hardware
   #
   
   [env:STM32F407VE_black]
   platform          = ststm32
   board             = blackSTM32F407VET6
   platform_packages = framework-arduinoststm32@>=3.107,<4
   build_flags       = ${common.build_flags}
    -DTARGET_STM32F4 -DARDUINO_BLACK_F407VE
    -DUSBCON -DUSBD_USE_CDC -DUSBD_VID=0x0483 -DUSB_PRODUCT=\"BLACK_F407VE\"
     -IMarlin/src/HAL/HAL_STM32
   build_unflags     = -std=gnu++11
   extra_scripts     = pre:buildroot/share/PlatformIO/scripts/generic_create_variant.py
   lib_ignore        = Adafruit NeoPixel, TMCStepper, SailfishLCD, SailfishRGB_LED, SlowSoftI2CMaster, SoftwareSerial
   src_filter        = ${common.default_src_filter} +<src/HAL/HAL_STM32>
   ```

   这里仅是简单的介绍一下几个必要的概念，剩余的内容请大家参考[`platformio`官方文档介绍---platformio.ini部分](https://docs.platformio.org/en/latest/projectconf.html)：

   - `board_dir`:指定板子描述文件的位置，`platformio`首先会根据指定位置寻找板子描述文件，找不到则到安装目录下寻找。这里指定了板子描述文件的位置：`buildroot/share/PlatformIO/boards`
   
   - `board`：指定板子描述文件的名称
   
     ![1582873331192](images\board_path.png)
   
     根据上面两点的指示我们可以准确的找到板子描述文件：`buildroot/share/PlatformIO/boards/blackSTM32F407VET6.json`。文件通过`JSON`消息描述了硬件的具体信息。这里我们注意一下19行的位置：指定了编译时需要的与板子相关的源文件的文件夹名称（后面会用到，这里知道即可）。
   
     ![1582873818202](images/variant_position.png)
   
     
   
   - `platform_packages`：指定编译的平台框架，这里用到的是`framework-arduinoststm32`，实际这是ST官方为STM32开发板使用Arduino平台开发的库。该库的结构很清晰整洁，兼容STM32全系列的芯片，里面已经包含了许多开发板样例，当然也可以仿照样例将自己的开发板添加到其中。
   
   - `extra_scripts     = pre:buildroot/share/PlatformIO/scripts/generic_create_variant.py`：这一行是执行python脚本文件，前面有一个前缀`pre:`表示在主脚本执行之前执行（这里可以理解为在编译之前执行即可）。该脚本文件可以在上述路径下找到。打开该文件后可以看到一段python原码，主要做了一件事情：将`buildroot/share/PlatformIO/variants`路径下的全部内容复制到，`C:\Users\{用户名}\.platformio\packages\framework-arduinoststm32\variants`路径下（针对于windows）。这些内容都是编译会用到的内容。还记得之前板子描述文件中提到过的`MARLIN_F407VE`吗？在`buildroot/share/PlatformIO/variants`目录下有一个名为`MARLIN_F407VE`的文件夹，这可不是恰巧同名，前面的名称就是指代的这个文件夹的名称。`MARLIN_F407VE`中存放了和硬件直接相关的源码配置文件。
   
2. 了解到上面的信息后，便可以根据自己的开发板仿照已有案例完成两项工作

   - 基于样例修改板子描述文件
   - 基于样板修改板子相关的源码文件

## 如何配置使用多个串口

   **--- 基于`framework-arduinoststm32`框架，以BLACK_F407VE为例**

现在marlin可以配置双串口支持，且可以支持串口屏（串口屏支持会在后续文章中讲解）。如果我们只是在marlin代码层配置了多串口，编译是会报错的。下面开始正文：

1. 打开`buildroot/share/PlatformIO/variants/MARLIN_F407VE`文件夹下的`variant.h`文件，在文件307行左右的`// UART Definitions`下添加如下使能即可：

   ```c
   #define ENABLE_HWSERIAL 2  //使能串口2
   #define ENABLE_HWAERIAL 3  //使能串口3
   ```

   这样配置完成后marlin开启多串口编译就不会报错了。

