# Chlorine 
# Time : 2022/10/29 16:37

"""
    1. 布尔数据类型
        True表示真
        False表示假
        True实际上就是1
        False实际上就是0

        变量名称 = bool类型的字面量

    2. 比较运算符号
        布尔类型的数据可以通过比较运算来获取
        比较运算符号: >, <, >=, <=, ==, !=

    3. 判断语句 if 的基本格式
        if 要判断的条件:
            条件成立的时候要做的事情（这里可以写任意行的语句，但是要求比if有tap缩进）
            if 的缩进非常重要，缩进会决定那些语句是在 if 的控制中

        注意：
            1. if 的判断结果必须为布尔类型
            2. if 判断语句在结束后，必须在后面有一个冒号
            3. python 通过缩进关系（4个空格）来判断代码块的归属关系

    4. if - else 的组合结构
        if 条件:
            statement1
            statement2
            ...
        else :
            statement1
            statement2
            ...

        注意：
            1. else后面没有判断条件
            2. else的代码块也需要有4个空格的缩进

    5. if - elif - else的多条件组合语法
        注意：
            1. 从条件 1 到条件 N 依次匹配，都不匹配才会进入 else 语句
            2. 条件只会被匹配一次，一旦其中一个if被匹配了，后面的 if 就不看了
            3. 最后的 else 是可以省略的
            4. 判断最好是互斥且有序的

        if 条件1:
            statement1
            statement2
            ...
        elif 条件2:
            statement1
            statement2
            ...
        elif 条件3:
            statement1
            statement2
            ...
        ...
        else:
            statement1
            statement2
            ...

    6. 判断语句的嵌套
        if con1:
            statement1:
            statement2:
            ...

            if con2: 只有条件1和条件2都满足的时候才会执行一下的语句
                statement1:
                statement2:
                ...
"""

###
num1 = 10
num2 = 10
print(num1 == num2)
print(num1 != num2)

name1 = "Hello"
name2 = "World"
print(name1 == name2)
###

###
age = 18

if age == 18:
    print("OK")
    print("Hello")
print("World")

if age != 18:
    print("OK")
    print("Hello")
print("World")
###

###
age = input("Tell me your age: ")
if int(age) >= 18:
    print("Pass")
else:
    print("Not Pass")
###

###
a = input("input a number: ")
if int(a) == 2:
    print("a == 2")
elif int(a) == 1:
    print("a == 1")
elif int(a) == 3:
    print("a == 3")
elif int(input("Tell me a number again")) == 4:
    print("a == 4")
###

###
a = int(input("give me a number"))
if a > 10:
    print("a is not Small")
    if a > 20:
        print("BIG")
    elif a < 15:
        print("Middle")
    else:
        print("Bigger than Small")
else:
    print("Small")
###

