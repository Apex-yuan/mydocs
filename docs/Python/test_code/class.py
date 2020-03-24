#!/usr/bin/env python3

# class MyClass:
#     '''
#     自定义类
#     '''
#     i = 12345
#     def f(self):
#         return 'hello world!'

# x = MyClass()

# print("i", x.i)
# print("f", x.f(),x.i)

### 运算符重载
# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __str__(self):
#         return 'Vector ({0}, {1})'.format(self.a, self.b)

#     def __add__(self,other):
#         return Vector(self.a + other.a, self.b + other.b)

# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print(v1 + v2)

### 类的属性和方法
# class Counter:
#     __secretCount = 0 # 私有变量
#     publicCount = 0 # 公有变量

#     def __prt(self,a):
#         print(a)

#     def count(self): # 公有方法
#         self.__secretCount += 1
#         self.publicCount += 1
#         self.__prt(self.__secretCount)

# counter = Counter()
# counter.count()
# counter.count()

### 继承
class People:
    name = ''
    __age = '0'
    __weight = '0'

    def __init__(self, name, age, weight):
        self.name = name
        self.__age = age
        self.__weight = weight

    def speak(self):
        print("my name is {},my age is {},my weight is {}".format(self.name, self.__age, self.__weight))

class Student(People):
    grade = ''

    def __init__(self,n, a, w, g):
        People.__init__(self,n, a, w)
        self.grade = g

    def speak(self): # 覆写父类的方法
        print("{} say: my grade is {}".format(self.name, self.grade))

s1 = Student("wang yuan", 27, 62, "two")
s1.speak()