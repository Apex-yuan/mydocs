#!/usr/bin/env python3
print("hello,world!")

print(2**10)

# name = input()
# print(name)

#单行注释

'''
多行注释：
窗前明月光
疑是地上霜
举头望明月
低头思故乡
'''

if True:
    print("True")
    print("keep going")
else: 
    print("False")
    print("give up")

#!/user/bin/env python3
item_one = 16
item_two = 13
item_three = 15
total = item_one + \
        item_two + \
        item_three

'''
python 数字类型：
- 布尔(bool:True/False)
-整数(int)表示长整形
-浮点数(float)
-复数（complex）
'''
a = """sdfsdfadew
lsdfsldfsf"""
print(a)

str = 'robot'
print(str[0:-1:2])

#导入整个模块
import sys
for i in sys.argv:
    print(i)
print(sys.argv)
# print("\n python 路径：", sys.path)

#导入特定的成员
from sys import argv,path
print('path:', path)
print('argv:', argv)