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

"""

###
for char in "Hello World":
    print(char)

a = "Hello World"
for b in a:
    print(b)
###
