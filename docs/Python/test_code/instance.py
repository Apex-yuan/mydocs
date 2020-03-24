# 1. 打印hello world
# print("hello world!")

# 2. 数字求和
# a = float(input("请输入第一个数字："))
# b = float(input("请输入第二个数字："))
# print("两数之和为：{}".format(a+b))

# 3. 平方根
# import math
# a = float(input("请输入一个数字："))
# print("{}的平方根为：{}".format(a, math.sqrt(a)))

# 4. 二次方程
# a = int(input("please input a:"))
# b = int(input("please input b:"))
# c = int(input("please input c:"))

# delta = b**2-4*a*c
# print(delta)

# if delta > 0:
#     print("方程有两个根：x1={},x2={}".format((-b+delta**0.5)/2,(-b-delta**0.5)/2))
# elif delta == 0:
#     print("方程有两个相同的根：x={}".format((-b+delta**0.5)/2))
# else:
#     print("方程无解")

# 5. 计算三角形面积
# a = float(input("请输入第一条边长："))
# b = float(input("请输入第二条边长："))
# c = float(input("请输入第三条边长："))

# s = (a + b + c) / 2 # 计算半周长

# area = (s*(s-a)*(s-b)*(s-c))**0.5
# print("边长为{},{},{}的三角形的面积为：{}".format(a, b, c, area))

# 6. 计算圆的面积
# import cmath
# r = float(input("请输入圆的半径r="))
# print("半径为{}的圆的面积为：{}".format(r, cmath.pi*r*r))

# 7. 随机数生成
# import random
# print("随机数：{}".format(random.random()))

def readBinFile(filename, list):
    f = open(filename, "rb")
    while True:
        byte = f.read(1)
        if len(byte) == 0:
            break
        else:
            list.append("0x{:02X}".format(ord(byte)))   #list_data.append("0x%.2X" % ord(t_byte))
    print(list)

list = []
readBinFile("tool.html.gz", list)

print(ord('a'))
