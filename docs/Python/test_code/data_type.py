#!/usr/bin/python3
'''
python 中变量不需要声明，每个变量在使用前必须赋值，变量赋值后该变量才会被创建
python 中变量就是变量没有类型，我们所说的“类型”是变量所指的内存中对象的类型
'''
counter = 100
miles   = 1000.0
name    = "apexyuan"
print(counter)
print(miles)
print(name)

'''
多变量赋值
'''
a = b = c = 100
print(a,b,c)
a, b, c = 1,2,"apexyuan"
print(a,b,c)

'''
标准数据类型：
- Number（数字）
- String（字符串）
- List（列表）
- Tuple（元组）
- Set（集合）
- Dictionary（字典）
可变数据：List, Dictionary, Set
不可变数据：Number, String, Tuple
'''

'''
Number:
python3中只有一个整数类型int，表示长整形
- 内置的type()函数可以用来查询变量所指的数据类型
数值的除法包含两个运算符：/返回一个浮点数 //返回一个整数（取商）
'''

苹果 = 3
print(苹果)

str = '''第一行
		第二行
		第三行'''
print(str)
print('hello\rworld!')
print(r'hello\rworld!')

print("hello " + "world!")
print("hello world!\n" * 3)
print(type(str))

list = ['abc', 123, 3.14, True]
add_list = ['hello', 'world']

print(list) #输出完整列表
print(list[2]) #输出列表的第二个元素
print(list[1:3]) #输出列表第二到第三个元素
print(list + add_list)
print(list * 2)

def reverseWords(input):
    # 通过空格将字符串分隔，将各个单词分割为列表
    inputWords = input.split(" ")
    
    inputWords = inputWords[-1::-1]
    
    output = '@'.join(inputWords)
    return output
if __name__ == "__main__":
    input = 'I like python'
    rw = reverseWords(input)
    print(rw)

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
# c = set('abc','abd')
# print(c)

dict = {}
dict['one'] = '1 - apex'
dict[2] = '2 - yuan'

info_dict = {'name':'xiaoyuan', 'code':1, 'gore':100}

print(dict['one'])
print(dict[2])
print(info_dict)
print((info_dict.keys()))
print(info_dict.values())

# #!/usr/bin/python3

# import sys

# def fibonacci(n):
#     a,b,counter = 0, 1, 0
#     while True:
#         if(counter > n):
#             return
#         yield a
#         a, b = b, a+b
#         counter += 1
# f = fibonacci(10)

# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()


for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
