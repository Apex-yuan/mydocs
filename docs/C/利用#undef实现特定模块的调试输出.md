# 利用`#undef`实现特定模块的调试输出

## Preface

在平时的编程中肯定会用到打印功能来调试自己的程序，调试的时候将打印函数取消注释，在调试完成后将打印函数注释掉。不知大家是如何处理的，我以前可一直是这么干的。这样处理第一太繁琐，第二影响程序的美观性。后面想了一个用`#if ... #endif`语法来封装`printf`函数的做法:

```c
#if DEBUG_MOUDEL
	print("debug moudel\n");
#endif
```

需要调试特定模块的时候只需在该模块文件的开头添加`#define DEBUG_MOUDEL`即可。但这样给写程序添加了很大的负担。

对于`#undef`，在这里我们知道他的书面意思就够了，与`#define`相对，解除对后面宏的定义。

## Instance

### `debug_out.h`

这是我们用于调试输出的核心文件，在需要调试的模块文件中要包含该文件，并在之前添加上`# define DEBUG_OUT`的宏定义便可开启该模块的调试。调试完成后只需将`#define DEBUG_OUT`的宏注释掉即可。

```c
#include <stdio.h>

//用于调试的串行别名。 
//用法：在给定的.cpp文件中定义DEBUG_OUT（或不定义）后，包括此标头
//用于特定模块（文件）的调试

#define NOOP //(void(0))

#undef DEBUG_PRINT

#if DEBUG_OUT
#define DEBUG_PRINT printf
#else 
#define DEBUG_PRINT(...) NOOP
#endif 

#undef DEBUG_OUT
```

### `moudel1`

`moudel1.h`

```c
#ifndef __MOUDEL1_H
#define __MOUDEL1_H

#define DEBUG_OUT  //调试MOUDEL1
#include "debug_out.h"

void moudel1(void);

#endif 
```

`moudel1.c`

```c
#include "moudel1.h"

void moudel1(void)
{
    DEBUG_PRINT("moudel1 debug...\n");
}
```

### `moude21`

`moudel2.h`

```c
#ifndef __MOUDEL2_H
#define __MOUDEL2_H

//#define DEBUG_OUT //不调试MOUDEL2
#include "debug_out.h"

void moudel1(void);

#endif 
```

`moudel2.c`

```c
#include "moudel2.h"

void moudel2(void)
{
    DEBUG_PRINT("moudel2 debug...\n");
}
```

### `main.c`

```c
#include <stdio.h>
#include "moudel1.h"
#include "moudel2.h"

int main(void)
{
    printf("test debug out:\n");
    moudel1();
    moudel2();

    return 0;
}
```

## 结果

```bash
C:\Users\username\Desktop\C_CPP\debug_test>gcc main.c moudel1.c moudel2.c -o main

C:\Users\username\Desktop\C_CPP\debug_test>.\main.exe
test debug out:
moudel1 debug...

```

-----

**`Note:`**

`#define DEBUT_OUT`只能定义在要调试的模块文件中才行，如果想在统一的文件中定义是否调试某个模块可以转一层定义，下面是一种思路：

```c
#define DEBUG_OUT defined(DEBUG_MOUDEL1)
```

在配置文件中定义`#define DEBUG_MOUDEL1`，只需在上面代码之前包含配置文件即可。

---

## 分析

针对于`moudel1.c`文件将所有的预处理展开后如下：

```c
/* moudel1.h start */
#ifndef __MOUDEL1_H
#define __MOUDEL1_H

#define DEBUG_OUT  //调试MOUDEL1
/* debug_out.h start */
#include <stdio.h>

//用于调试的串行别名。 
//用法：在给定的.cpp文件中定义DEBUG_OUT（或不定义）后，包括此标头
//用于特定模块（文件）的调试

#define NOOP //(void(0))

#undef DEBUG_PRINT

#if DEBUG_OUT
#define DEBUG_PRINT printf
#else 
#define DEBUG_PRINT(...) NOOP
#endif 

#undef DEBUG_OUT
/* debug_out end */
void moudel1(void);

#endif 
/* moudel1.h end */
void moudel1(void)
{
    DEBUG_PRINT("moudel1 debug...\n");
}
```

首先定义了`DEBUG_OUT`自然条件编译在选择时是`#define DEBUG_PRINT printf`故该模块中的`DEBUG_PRINT`当做`printf`对待。后面又有一句`#udef DEBUG_OUT`解除对DEBUG_OUT的定义故对其他未定义`DEBUG_OUT`的模块，预处理中条件编译的选择是`#define DEBUG_PRINT(...) NOOP`,即`DEBUG_PRINT`是一个空函数。