# 基于`vscode`搭建`STM32`编译调试环境(`Windows`)

## 安装工具

1. `vscode`

2. `STM32cubeMX`

   用来生成带`Makefile`的代码工程

3. `git`

   git是一个非常出名的分布式版本管理工具，很有必要学习使用，但这里主要是为了使用其`bash`终端，其用法类似于`linux`的`shell`，而Makefile文件中使用的命令（如：`clean`）习惯为为linux shell执行的命令,比`Windows`的`cmd`和`powershell`具有更好的通用性。

4. `mingw-w64`

   安装过程可参考https://blog.csdn.net/itas109/article/details/99699426，https://www.jianshu.com/p/a6e0d1465491，这里主要用到其`make`工具。

5. `ARM GCC Toolchain`

   编译工具链，最终的可执行文件就要利用这些工具链生成。 

6. `OpenOCD`

   [OpenOCD User’s Guide](http://openocd.org/doc-release/html/#toc-Flash-Programming-1)

   将编译生成的目标文件下载到芯片内；结合`ARM GCC Toolchain`的`gdb`模块实现在线调试功能。

## 流程简介



