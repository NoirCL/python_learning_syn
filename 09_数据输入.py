# Chlorine 
# Time : 2022/10/29 16:27

"""
    使用input()从键盘获取输入
    使用一个变量来接收从input中获取的数据，接受到的数据默认为字符串类型

    input语句可以直接给出提示：input(str)

    如果输入的数字类型，结果仍然是字符串类型
"""

name = input()
print(name)

name = input("Tell me your name: ")
print(name)

number = input("give me a number: ")
print(type(number), number)
print(type(int(number)), int(number))
