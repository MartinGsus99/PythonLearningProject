import os


def read_my_input():
    str=input("请输入：")
    print("Input:",str)
    return  str


def read_local_file():
    file=open("test.txt", "r+")
    print(file.read())
    strs=read_my_input()
    file.write(strs)
    file.close()

read_local_file()
