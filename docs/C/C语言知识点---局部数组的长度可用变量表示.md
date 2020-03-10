# C语言知识点---局部数组的长度可以用变量来定义

首先我们知道C语言中，全局数组在定义的时候必须给定长度，而且长度必须是常量。一直没注意函数内部的局部数组在定义的时候长度可以为变量。具体见下例：

```c
#include <stdio.h>
#include <stdint.h>

int main(void)
{
    int a = 5;
    uint8_t tmp[a];  //变量a作为tmp数组的长度 
    
    for(int i = 0; i < a; ++i)
    {
        tmp[i] = i;
        printf("tmp[%d]=%d ",i, tmp[i]);
    }
    printf("\n");
    return 0;
}
```

`gcc`编译器输出如下

```bash
C:\Users\username\Desktop\C_CPP>gcc local_arry.c -o local_arry

C:\Users\username\Desktop\C_CPP>.\local_arry.exe
tmp[0]=0 tmp[1]=1 tmp[2]=2 tmp[3]=3 tmp[4]=4
```

