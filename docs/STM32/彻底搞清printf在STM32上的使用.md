# 彻底搞清`printf`在`STM32`上的使用

[TOC]

## 重定向`printf`

### ARMCC版本（keil MDK）

下面这段代码，在实现串口发送一个字节的函数后，可以在勾不勾选”微库“的情况下都可以正常使用`printf`函数。`__MICROLIB`是勾选微库后会被定义的宏，因而可以通过条件编译的方式兼容。

```c
#if !defined(__MICROLIB)
#pragma import(__use_no_semihosting)
void _sys_exit(int x) //避免使用半主机模式
{
  x = x;
}
struct __FILE
{
  int handle;
};
FILE __stdout;
#endif

#ifdef __GNUC__
#define PUTCHAR_PROTOTYPE int __io_putchar(int ch)
#else
#define PUTCHAR_PROTOTYPE int fputc(int ch, FILE *f)
#endif 
PUTCHAR_PROTOTYPE
{
  /* 实现串口发送一个字节数据的函数 */
  serial_write(&serial1, (uint8_t)ch); //发送一个自己的数据到串口
  return ch;
}
```

### ARMGCC版本（GCC）

ARMGCC库对printf函数的实现和ARMCC对printf函数的实现底层是不一样的，因而重定向的底层实现也有区别。

```c
#ifdef __GNUC__
#define PUTCHAR_PROTOTYPE int __io_putchar(int ch)
#else
#define PUTCHAR_PROTOTYPE int fputc(int ch, FILE *f)
#endif 
{
    /* 实现串口发送一个字节数据的函数 */
    serial_write(&serial1, (uint8_t)ch); //发送一个自己的数据到串口
    return ch;
}

int _write(int file, char *ptr, int len)
{
	int DataIdx;
	for(DataIdx = 0; DataIdx < len; DataIdx++)
	{
		PUTCHAR_PROTOTYPE(*ptr++);
	}
	return len;
}
```



## 重写`printf`

如果在使用多个串口的过程中都想是想用printf函数可以通过下面的方式来实现，只不过就不要使用printf的函数名了。

```c
/* 用于实现自己的printf函数的原型 */
#include <stdarg.h>
#include <string.h> 
#include <stdio.h>

void serial2_printf( const char * format, ... )
{
  char buffer[256];
  va_list args;
  va_start (args, format);
  vsprintf (buffer,format, args);
  //send_via_USART1 (buffer);
  uint8_t len = strlen((const char*)buffer);
  for(uint8_t i = 0; i < len; ++i)
  {
    /* 通过串口发送一个字节的数据 */
    serial_write(&serial2, (uint8_t)buffer[i]);
  }
  va_end (args);
}
```

