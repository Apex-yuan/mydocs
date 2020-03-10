# python learing
## 安装

## 简介

在脚本顶部添加以下命令可以让python脚本像shell脚本一样直接可执行

```python
#!/usr/bin/env python3
```

修改脚本权限

```bash
$ chmod +x hello.py
```

执行脚本

```bash
./hello.py
```





## 语法

### 编码

默认情况下，python3源码文件以UTF-8编码，所有的字符串都是unicode字符串。也可以为源码文件指定不同的编码:

```python
# -*- coding: cp-1252 -*-
```

### 标识符

和C语言一致

### 关键字
```python
>>> import keyword
>>> keyword.kwlist # 输出所有的关键字
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```
### 注释
```python
# 单行注释

print('hello world!') # 注释

'''
多行注释1
多行注释2
多行注释3
'''

"""
多行注释1
多行注释2
多行注释3
"""
```
###  行与缩进

python使用缩进来表示代码块，缩进的空格是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。

```python
if True:
    print('True')
else:
    print('False')
```

### 多行语句

python 通常是一行写一条完整语句，如果语句很长，可以使用反斜杠(\\)来实现多行语句：

```python
sum = a + \
	  b + \
      c
```

### 一行显示多条语句

python可以在一行中使用多条语句，中间使用分号(;)隔开

```python
print("hello"); print("TOM"); print("China")
```

### print

print默认是输出换行的，如果要实现不换行，需要在变量末尾加上end="":

```python
print("hello ", end="")
print("world!")
```

### import与from...import

- 将整个模块(somemodule)导入： `import somemodule`
- 从某个模块中导入某个函数：`from somemodule import somefunction`
- 从某个模块中导入多个函数：`from somemodule import firstfunc, secondfunc thirdfunc`
- 导入某个模块的全部函数：`from somemodule import *`

### 多变量赋值

```python
#创建一个整形对象，值为1，从右向左赋值，三个变量都被富裕相同的数值
a = b = c = 1;
#两个整形对象分别赋值给a和b，字符串对象赋值给c
a, b, c = 1, 2, "apexyuan"
```



## 数据类型

python 中变量不需要声明，每个变量在使用前必须赋值，变量赋值后该变量才会被创建

python 中，变量就是变量没有类型，我们所说的“类型”是变量所指的内存中对象的类型

### 标准的数据类型

- Number（数字）
- String（字符串）
- List（列表）
- Tuple（元组）
- Set（集合）
- Dictionary（字典）

其中：

- 不可变数据类型：Number, String, Tuple
- 可变数据类型：List, Dictionary,Set

---

**`Note`**

内置的`type()`函数可以查询变量所指的对象的类型

```python
str = 'python'
print(type(str))
```



---

### Number

- `int`: python3中只有一种整形int，表示长整形。
- `float`: 3.14
- `bool`: True/False
- `complex`: 1+2j

- 

---

**`Note`**

- 数值的除法包括两个运算符：`/`返回一个浮点数，`//`返回一个整数。
- 混合计算时，python会把整形数转换成浮点数。
- 一个变量可以通过赋值指向不同类型的对象

```python
print(9 / 2) #除法
print(9 // 2) #取商
print(9 % 2) #取余
print(2 ** 5) #乘方

a = 12 #整数
print(a)
a = 'string' #字符串
print(a)
```

---



### String

字符串使用单引号`’`或双引号`“`括起来，同事使用反斜杠`\`转义特殊字符。

- 单引号和双引号的用法完全相同

- 使用三引号(`'''`或`”“”`)可以指定一个多行字符串

- `\`用来转义，使用r可以让`\`不发生转义。如：r"hello\nworld!"，\n会显示并不会换行。（注：`r`为raw的意思）

- 可以用`+`运算符连接字符串，用`*`运算符重复。

- 字符串有两种索引方式：从左往右以0开始，从右往左以-1开始。

  ```
    0   1   2   3   4   5
   -6  -5  -4  -3  -2  -1
  +---+---+---+---+---+---+
  | p | y | t | h | o | n |
  +---+---+---+---+---+---+
  ```

  

- 没有单独的字符类型，一个字符就是长度为1的字符串

- 字符串截取的语法：`变量[头下标:尾下标:步长]`

- 字符串不可更改，即字符串中的元素是不可以改变的

```python
print('python')
print("python")

str = '''第一行
第二行
第三行'''
print(str)

print('hello\rworld!')
print(r'hello\rworld!')

print("hello " + "world!")
print("hello world!\n" * 3)

str = 'python'
print(str[0:3])
print(str[:3])
print(str[2:-1])
print(str[0:5:2])
```

### List

- 列表是卸载方括号`[]`之间，用逗号`,`分隔开的元素列表
- 列表中元素的类型可以不相同，支持数字，字符串，甚至可以包含列表
- 和字符串一样，列表也可以被索引和截取，截取语法`变量[头下标:尾下标:步长]`（若步长为负数，则表示逆向读取）

```python
#!/usr/bin/env python3

list = ['abc', 123, 3.14, True]
add_list = ['hello', 'world']

print(list)            #输出完整列表
print(list[2])         #输出列表的第二个元素
print(list[1:3])       #输出列表第二到第三个元素组成的列表
print(list + add_list) #输出连接列表
print(list * 2)        #输出复制n次后的列表
```

---

**`Note`**

- 与字符串的不同点：列表中的元素是可以改变的。

---

```python
def reverseWords(input):
    # 通过空格将字符串分隔，将各个单词分割为列表
    inputWords = input.split(" ")
    '''
    inputWords[-1::-1]
    第一个参数-1，表示最后一个元素
    第二个参数为空，表示移动到列表末尾
    第三个参数为步长，-1表示逆向
    '''
    inputWords = inputWords[-1::-1]
    
    output = ' '.join(inputWords)
    return output
if __name__ == "__main__":
    input = 'I like python'
    rw = reverseWords(input)
    print(rw)
```

### Tuple

元组与列表类似，不同之处在于**元组的元素不能更改**。元组写在小括号`()`里，元素之间用逗号隔开。

```python
#!/usr/bin/env python3

tuple = ('abc', 123, 3.14, True)
add_tuple = ('ced', 456)

print(tuple) #打印完整元组
print(tuple[2])
print(tuple[1:3])
print(tuple * 2)
print(tuple + add_tuple)
```

---

**`Note`**

- 可以把字符串看做是一种特殊的元组**

- 虽然tuple的元素不可以改变，但他可以包含可变的对象，比如list列表。

- 构造包含0或1个元素的元组比较特殊，所以有一些额外的语法规则：

  ```python
  tup1 = () #空元组
  tup2 = (1,) # 一个元素，需要在元素后添加逗号
  ```

---

### Set

集合是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员

可以使用`{}`或`set()`函数创建集合，注意：创建一个空集合必须用`set()`

```python
#!/usr/bin/python3

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jake', 'Rose'}
print(student) #输出集合，重复的元素被自动去掉

#成员测试
if 'Rose' in student :
    print('Rose在集合中')
else:
    print('Rose不在集合中')
    
# set可以进行集合运算
a = set('abraabraabcd')
b = set('alacazam')
print(a)
print(a - b) # a和b的差集
print(a | b) # a和b的并集
print(a & b) # a和b的交集
print(a ^ b) # a和b中不同时存在的元素
```

### Dictionary

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别：字典中的元素是通过建来存取的，而不是通过偏移存取的。

字典是一种映射类型，字典用`{}`标识，它是一个无序的键(key):值(value)的集合。键必须使用不可变的类型。同一字典中，键(key)必须是唯一的。

```python
dict = {}
dict['one'] = '1 - apex'
dict[2] = '2 - yuan'

info_dict = {'name':'xiaoyuan', 'code':1, 'gore':100}

print(dict['one'])
print(dict[2])
print(info_dict)
print(info_dict.keys())
print(info_dict.values())
```

### 内置的数据类型转换

| 函数                                                         | 描述                                                |
| :----------------------------------------------------------- | :-------------------------------------------------- |
| [int(x [,base\])](https://www.runoob.com/python3/python-func-int.html) | 将x转换为一个整数                                   |
| [float(x)](https://www.runoob.com/python3/python-func-float.html) | 将x转换到一个浮点数                                 |
| [complex(real [,imag\])](https://www.runoob.com/python3/python-func-complex.html) | 创建一个复数                                        |
| [str(x)](https://www.runoob.com/python3/python-func-str.html) | 将对象 x 转换为字符串                               |
| [repr(x)](https://www.runoob.com/python3/python-func-repr.html) | 将对象 x 转换为表达式字符串                         |
| [eval(str)](https://www.runoob.com/python3/python-func-eval.html) | 用来计算在字符串中的有效Python表达式,并返回一个对象 |
| [tuple(s)](https://www.runoob.com/python3/python3-func-tuple.html) | 将序列 s 转换为一个元组                             |
| [list(s)](https://www.runoob.com/python3/python3-att-list-list.html) | 将序列 s 转换为一个列表                             |
| [set(s)](https://www.runoob.com/python3/python-func-set.html) | 转换为可变集合                                      |
| [dict(d)](https://www.runoob.com/python3/python-func-dict.html) | 创建一个字典。d 必须是一个 (key, value)元组序列。   |
| [frozenset(s)](https://www.runoob.com/python3/python-func-frozenset.html) | 转换为不可变集合                                    |
| [chr(x)](https://www.runoob.com/python3/python-func-chr.html) | 将一个整数转换为一个字符                            |
| [ord(x)](https://www.runoob.com/python3/python-func-ord.html) | 将一个字符转换为它的整数值                          |
| [hex(x)](https://www.runoob.com/python3/python-func-hex.html) | 将一个整数转换为一个十六进制字符串                  |
| [oct(x)](https://www.runoob.com/python3/python-func-oct.html) | 将一个整数转换为一个八进制字符串                    |