# Chlorine 
# Time : 2022/10/31 20:23

# 产生随机数的包为random包，通过import进行引入
import random

"""
    1. 循环的要素：
        1. 条件
        2. 动作
        3. 只要条件满足，会无限执行动作
    2. while语句：
        while con:
            statement1:
            statement2:
            ...
    3. while的注意：
        1. while的条件必须为bool类型
        2. 必须设置循环的终止条件，否则会无限循环
        3. while的内部语句必须缩进
    
    4. while也可也被嵌套
"""

###
a = 1
while a != 10:
    print(a)
    a += 1
###

###
a = -1
num = random.randint(1, 100)
print(f"Number is {num}")

while int(a) != num:
    a = int(input("Give me a number"))
    if a != num:
        print("Wrong number")
    else:
        print("Right number")
###

###
###
