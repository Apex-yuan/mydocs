print('hello world!')

# 海象运算符:=测试
# a = []
# for i in range(0,12):
#     a.append(i)
# if(n := len(a)) > 10:
#     print(f"List is too long ({n} elements, expeted <= 10)")

# 身份运算符is is not 测试
# a = 20
# b = 20
# b = 30
# if a is b:
#     print(f"a{id(a)} and b{id(b)} are the same")
# else:
#     print(f"a{id(a)} and b{id(b)} are different")

# 斐波那契数列
# c = [0,1]
# for i in range(1,50):
#     c.append(c[i] + c[i-1])
# print(c)
# print(len(c))

# 迭代器
# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a < 20:    
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration

# myclass = MyNumber()
# it = iter(myclass)

# # print(next(myclass))
# # print(myclass.a)
# for x in it:
#     print(x)

# 函数参数
def printInfo(name,number):
    print(name)
    print(number)
    return

printInfo(number = 1314410833, name = "wangyuan")