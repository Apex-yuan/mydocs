# runoob python learing note

基于python3

## 一、简介

Python是一种**解释性**、**交互式**、**面向对象**的脚本语言。Python 是由 Guido van Rossum 在八十年代末和九十年代初，在荷兰国家数学和计算机科学研究所设计出来的。

## 二、环境搭建

### 安装Python

### Python环境变量

| 变量名        | 描述                                                         |
| :------------ | :----------------------------------------------------------- |
| PYTHONPATH    | PYTHONPATH是Python搜索路径，默认我们import的模块都会从PYTHONPATH里面寻找。 |
| PYTHONSTARTUP | Python启动后，先寻找PYTHONSTARTUP环境变量，然后执行此变量指定的文件中的代码。 |
| PYTHONCASEOK  | 加入PYTHONCASEOK的环境变量, 就会使python导入模块的时候不区分大小写. |
| PYTHONHOME    | 另一种模块搜索路径。它通常内嵌于的PYTHONSTARTUP或PYTHONPATH目录中，使得两个模块库更容易切换。 |

### 运行Python

- 交互式运行

- 脚本式运行

  ---

  **`Note:`**

  在脚本顶部添加以下命令可以让python脚本像shell脚本一样直接可执行（linux环境下）

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

  ---

## 三、基础语法

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

### pass语句

Python中pass是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句。

## 四、基本数据类型

python 中变量不需要声明，<u>每个变量在使用前必须赋值</u>，**变量赋值后该变量才会被创建**。

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

#### 数据类型转换

- **int(x)** 将x转换为一个整数。
- **float(x)** 将x转换到一个浮点数。
-  **complex(x)** 将x转换到一个复数，实数部分为 x，虚数部分为 0。
- **complex(x, y)** 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。

#### 数学函数

| 函数                                                         | 返回值 ( 描述 )                                              |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [abs(x)](https://www.runoob.com/python3/python3-func-number-abs.html) | 返回数字的绝对值，如abs(-10) 返回 10                         |
| [ceil(x) ](https://www.runoob.com/python3/python3-func-number-ceil.html) | 返回数字的上入整数，如math.ceil(4.1) 返回 5                  |
| cmp(x, y)                                                    | 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 **Python 3 已废弃，使用 (x>y)-(x。 |
| [exp(x) ](https://www.runoob.com/python3/python3-func-number-exp.html) | 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045         |
| [fabs(x)](https://www.runoob.com/python3/python3-func-number-fabs.html) | 返回数字的绝对值，如math.fabs(-10) 返回10.0                  |
| [floor(x) ](https://www.runoob.com/python3/python3-func-number-floor.html) | 返回数字的下舍整数，如math.floor(4.9)返回 4                  |
| [log(x) ](https://www.runoob.com/python3/python3-func-number-log.html) | 如math.log(math.e)返回1.0,math.log(100,10)返回2.0            |
| [log10(x) ](https://www.runoob.com/python3/python3-func-number-log10.html) | 返回以10为基数的x的对数，如math.log10(100)返回 2.0           |
| [max(x1, x2,...) ](https://www.runoob.com/python3/python3-func-number-max.html) | 返回给定参数的最大值，参数可以为序列。                       |
| [min(x1, x2,...) ](https://www.runoob.com/python3/python3-func-number-min.html) | 返回给定参数的最小值，参数可以为序列。                       |
| [modf(x) ](https://www.runoob.com/python3/python3-func-number-modf.html) | 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。 |
| [pow(x, y)](https://www.runoob.com/python3/python3-func-number-pow.html) | x**y 运算后的值。                                            |
| [round(x [,n\])](https://www.runoob.com/python3/python3-func-number-round.html) | 返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。 **其实准确的说是保留值将保留到离上一位更近的一端。** |
| [sqrt(x) ](https://www.runoob.com/python3/python3-func-number-sqrt.html) | 返回数字x的平方根。                                          |

#### 随机数函数

| 函数                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [choice(seq)](https://www.runoob.com/python3/python3-func-number-choice.html) | 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。 |
| [randrange ([start,\] stop [,step]) ](https://www.runoob.com/python3/python3-func-number-randrange.html) | 从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1 |
| [random() ](https://www.runoob.com/python3/python3-func-number-random.html) | 随机生成下一个实数，它在[0,1)范围内。                        |
| [seed([x]) ](https://www.runoob.com/python3/python3-func-number-seed.html) | 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。 |
| [shuffle(lst) ](https://www.runoob.com/python3/python3-func-number-shuffle.html) | 将序列的所有元素随机排序                                     |
| [uniform(x, y)](https://www.runoob.com/python3/python3-func-number-uniform.html) | 随机生成下一个实数，它在[x,y]范围内。                        |

#### 三角函数

| 函数                                                         | 描述                                               |
| :----------------------------------------------------------- | :------------------------------------------------- |
| [acos(x)](https://www.runoob.com/python3/python3-func-number-acos.html) | 返回x的反余弦弧度值。                              |
| [asin(x)](https://www.runoob.com/python3/python3-func-number-asin.html) | 返回x的反正弦弧度值。                              |
| [atan(x)](https://www.runoob.com/python3/python3-func-number-atan.html) | 返回x的反正切弧度值。                              |
| [atan2(y, x)](https://www.runoob.com/python3/python3-func-number-atan2.html) | 返回给定的 X 及 Y 坐标值的反正切值。               |
| [cos(x)](https://www.runoob.com/python3/python3-func-number-cos.html) | 返回x的弧度的余弦值。                              |
| [hypot(x, y)](https://www.runoob.com/python3/python3-func-number-hypot.html) | 返回欧几里德范数 sqrt(x*x + y*y)。                 |
| [sin(x)](https://www.runoob.com/python3/python3-func-number-sin.html) | 返回的x弧度的正弦值。                              |
| [tan(x)](https://www.runoob.com/python3/python3-func-number-tan.html) | 返回x弧度的正切值。                                |
| [degrees(x)](https://www.runoob.com/python3/python3-func-number-degrees.html) | 将弧度转换为角度,如degrees(math.pi/2) ，  返回90.0 |
| [radians(x)](https://www.runoob.com/python3/python3-func-number-radians.html) | 将角度转换为弧度                                   |

#### 数学常量

| 常量 | 描述      |
| ---- | --------- |
| pi   | 圆周率π   |
| e    | 自然常数e |



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
| int(x [,base\])                                              | 将x转换为一个整数                                   |
| [float(x)](https://www.runoob.com/python3/python-func-float.html) | 将x转换到一个浮点数                                 |
| complex(real [,imag\])                                       | 创建一个复数                                        |
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

## 五、运算符

### 算数运算符(+ - * / ** % //)

| 运算符 | 描述                                            | 实例               |
| :----- | :---------------------------------------------- | :----------------- |
| +      | 加 - 两个对象相加                               | a + b 输出结果 31  |
| -      | 减 - 得到负数或是一个数减去另一个数             | a - b 输出结果 -11 |
| *      | 乘 - 两个数相乘或是返回一个被重复若干次的字符串 | a * b 输出结果 210 |
| /      | 除 - x 除以 y                                   | b / a 输出结果 2.1 |
| %      | 取模 - 返回除法的余数                           | b % a 输出结果 1   |
| **     | 幂 - 返回x的y次幂                               | a**b 为10的21次方  |
| //     | 取整除 - 向下取接近商的整数                     | 9//2为4，-9//2为-5 |

### 关系运算符(== != > < >= <=)

| 运算符 | 描述                                                         | 实例                  |
| :----- | :----------------------------------------------------------- | :-------------------- |
| ==     | 等于 - 比较对象是否相等                                      | (a == b) 返回 False。 |
| !=     | 不等于 - 比较两个对象是否不相等                              | (a != b) 返回 True。  |
| >      | 大于 - 返回x是否大于y                                        | (a > b) 返回 False。  |
| <      | 小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。 | (a < b) 返回 True。   |
| >=     | 大于等于 - 返回x是否大于等于y。                              | (a >= b) 返回 False。 |
| <=     | 小于等于 - 返回x是否小于等于y。                              | (a <= b) 返回 True。  |

### 赋值运算符

| 运算符 | 描述                                                         | 实例                                  |
| :----- | :----------------------------------------------------------- | :------------------------------------ |
| =      | 简单的赋值运算符                                             | c = a + b 将 a + b 的运算结果赋值为 c |
| +=     | 加法赋值运算符                                               | c += a 等效于 c = c + a               |
| -=     | 减法赋值运算符                                               | c -= a 等效于 c = c - a               |
| *=     | 乘法赋值运算符                                               | c *= a 等效于 c = c * a               |
| /=     | 除法赋值运算符                                               | c /= a 等效于 c = c / a               |
| %=     | 取模赋值运算符                                               | c %= a 等效于 c = c % a               |
| **=    | 幂赋值运算符                                                 | c \**= a 等效于 c = c ** a            |
| //=    | 取整除赋值运算符                                             | c //= a 等效于 c = c // a             |
| :=     | 海象运算符，可在表达式内部为变量赋值。**Python3.8 版本新增运算符**。 | 示例如下                              |

`:=`示例，该表达式可以避免调用`len()`两次

```python
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
```



### 逻辑运算符

| 运算符 | 逻辑表达式 | 描述                                                         | 实例                    |
| :----- | :--------- | :----------------------------------------------------------- | :---------------------- |
| and    | x and y    | 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。 | (a and b) 返回 20。     |
| or     | x or y     | 布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。 | (a or b) 返回 10。      |
| not    | not x      | 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。 | not(a and b) 返回 False |

### 位运算符

| 运算符 | 描述                                                         | 实例                                                         |
| :----- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| &      | 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0 | (a & b) 输出结果 12 ，二进制解释： 0000 1100                 |
| \|     | 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。 | (a \| b) 输出结果 61 ，二进制解释： 0011 1101                |
| ^      | 按位异或运算符：当两对应的二进位相异时，结果为1              | (a ^ b) 输出结果 49 ，二进制解释： 0011 0001                 |
| ~      | 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。**~x** 类似于 **-x-1** | (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。 |
| <<     | 左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。 | a << 2 输出结果 240 ，二进制解释： 1111 0000                 |
| >>     | 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数 | a >> 2 输出结果 15 ，二进制解释： 0000 1111                  |

### 成员运算符

| 运算符 | 描述                                                    | 实例                                              |
| :----- | :------------------------------------------------------ | :------------------------------------------------ |
| in     | 如果在指定的序列中找到值返回 True，否则返回 False。     | x 在 y 序列中 , 如果 x 在 y 序列中返回 True。     |
| not in | 如果在指定的序列中没有找到值返回 True，否则返回 False。 | x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。 |

### 身份运算符

身份运算符用于比较两个对象的存储单元

| 运算符 | 描述                                        | 实例                                                         |
| :----- | :------------------------------------------ | :----------------------------------------------------------- |
| is     | is 是判断两个标识符是不是引用自一个对象     | **x is y**, 类似 **id(x) == id(y)** , 如果引用的是同一个对象则返回 True，否则返回 False |
| is not | is not 是判断两个标识符是不是引用自不同对象 | **x is not y** ， 类似 **id(a) != id(b)**。如果引用的不是同一个对象则返回结果 True，否则返回 False。 |

---

**`Note:`**

`id()`函数用于获取对象的内存地址

---

### 运算符优先级

| 运算符                   | 描述                                                   |
| :----------------------- | :----------------------------------------------------- |
| **                       | 指数 (最高优先级)                                      |
| ~ + -                    | 按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@) |
| * / % //                 | 乘，除，求余数和取整除                                 |
| + -                      | 加法减法                                               |
| >> <<                    | 右移，左移运算符                                       |
| &                        | 位 'AND'                                               |
| ^ \|                     | 位运算符                                               |
| <= < > >=                | 比较运算符                                             |
| == !=                    | 等于运算符                                             |
| = %= /= //= -= += *= **= | 赋值运算符                                             |
| is is not                | 身份运算符                                             |
| in not in                | 成员运算符                                             |
| not and or               | 逻辑运算符                                             |

## 六、流程控制

### 条件语句

### 循环语句

#### while

```python
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
```

#### for

for循环可以遍历任何序列的项目

```python
for <variable> in <sequence>:
    <statements>
else:
    <statements>
```

#### break / continue

## 七、迭代器和生成器

### 迭代器

迭代器是一个可以记住遍历位置的对象。迭代器对象从集合的第一个元素开始访问，知道所有的元素被访问结束。迭代器只能往前不能后退。

迭代器有两个基本的方法：

- `iter()`：创建迭代器对象

- `next()`：指向迭代器的下一个元素

---

**`Note:`**

`Stopiteration`异常用于标识迭代的完成，防止出现无限循环的情况。

```python
class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:   # 迭代20次终止
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumber()
it = iter(myclass)

for x in it:
    print(x)
```



---

### 生成器

python中使用了`yield`的函数被称为生成器（generator）。跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作。

在调用生成器运行的过程中，每次遇到yield时函数，会暂停并保存当前所有的运行信息，返回yield的值，并在下一次执行next()方法时从当前位置继续运行。

example：

```python
#!/usr/bin/python3
 
import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
```

## 八、函数

```python
def 函数名 (参数列表):
    函数体
```



## 九、数据结构



## 十、文件



## 十一、OS



## 十二、面向对象



## 十三、命名空间/作用域



## 十四、模块和标准库