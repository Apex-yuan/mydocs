#!/usr/bin/env python3

# fo = open("foo.txt", "w") # open file
# print("fo.name", fo.name)
# print("fo.mode", fo.mode)
# print("fo.closed",fo.closed)
# fo.write("fo.name:" + fo.name + "\n")
# fo.write("fo.mode:" + fo.mode + "\n")
# fo.write("fo.closed:" + str(fo.closed) + "\n")
# fo.close() # close file

# fo = open("foo.txt", "r")
# print("fo.readable:", fo.readable())
# # print("fo.readline:", fo.readline())
# # print("fo.readline:", fo.readline())
# str = fo.readline()
# aa = str.split(":")
# print(aa[1])
# fo.close()

# f.readlines() test
f = open("foo.txt", "r")
str = f.readline()
print(str)
str = f.readline()
print(str)
str = f.readline()
str = f.readline()
if str == "":
    print("end")
else:
    print("not end")
f.close()