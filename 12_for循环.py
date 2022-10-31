# Chlorine 
# Time : 2022/10/31 20:58

"""
    1. for 和 while的区别：
        1. for循环是一种轮询的机制，是对一批内容就进行逐个处理的模式
        2. while循环的条件是自定义的，自行控制循环条件

    2. for语句
        for 临时变量 in 待处理的数据集（序列 ）：
            statement

    3. for循环被称为遍历循环

    4. for循环无法定义循环条件，只能依次取出内容进行处理（所以被处理的数据集不可以无限大）

    5. range语句
        range 语句可以获得一个简单的数字序列
            1. range(num1) 获得 [0, num1) 的数字序列
            2. range(num1, num2) 获得 [num1, num1) 的数字
            3. range(num1, num2, step) 获得 [num1, num1) 的步长为step的数字

"""

###
for char in "Hello World":
    print(char)

a = "Hello World"
for b in a:
    print(b)
###

###
for x in range(5):
    print(x)

for x in range(1, 5):
    print(x)

for x in range(1, 5, 2):
    print(x)
for x in range(1, 5, 10):
    print(x)
for x in range(1, 5, 1):
    print(x)
###
