#!/usr/bin/env python3

var1 = 'hello world!'
var2 = "I love python"

print('var1[2:5]',var1[2:5])
print('var2[-1::-1]',var2[-1::-1])

print(var1[:6] + 'xiaoyuan')

if 'he' in var1:
    print(True)
else:
    print(False)

print('sd'.capitalize())
print('python sdf dfsd sdf'.count('fs'))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))