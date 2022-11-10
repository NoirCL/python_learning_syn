# Chlorine 
# Time : 2022/10/31 21:44

"""
    1. 函数：函数是组织好的，可以重复使用的，用来实现特定功能的代码段

    2. 使用函数的好处在于：
        1. 将功能封装在函数内部，可以随时重复使用
        2. 提高代码的复用性，减少重复代码，提高开发的效率

    3. 函数的定义语法：
        def 函数名(传入参数):
            函数体
            return 返回值（这个并不是必要的）

    4. 函数的调用：
        函数名(传入的参数)

    5. 函数的注意事项：
        1. 参数如果不需要，可以省略
        2. 返回值如果不需要，可以省略
        3. 函数必须先定义后使用
        4. 函数的定义必须在使用函数之前

    6. 函数的参数传入：
        定义：
            1. 在函数进行计算的时候，接收外部提供的数据
                def add():
                    result = 1 + 2
                    print(f"ans is {result}")
            2. 可以修改为：
                def add(a, b) :
                    result = a + b
                    print(f"{a} + {b} = {result}")
        注意：
            1. 定义的时候给出的a和b称为形式参数
                形式参数之间通过逗号进行分隔
            2. 函数调用的时候提供的a和b是实际参数，传入的时候按照顺序进行数据的传入，使用逗号进行分隔
                传入的时候给定的a和b是函数真正使用来计算的参数
            3. 参数的传入的数量是不受限制的
                1. 可以不使用参数
                2. 可以使用任意个参数

        7. 函数的返回值
            def add():
                result = 1 + 2
                print(f"ans is {result}")
                return result
            r = add()

            1. 定义：
                程序在完成后，给调用者的结果
            2. 语法：
                def 函数():
                    statement
                    return value
                变量 = 函数()
            3. return语句之后的内容是不会被执行的

"""

name = "Hello World"
print(len(name))

# len是py内置的函数

# 自己统计字符串的长度
a = 0
for x in name:
    a += 1
print(a)


# 自己定义一个函数
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(count)
    return count  # 返回统计的结果count


print(my_len(name))  # 输出my_len函数的返回值


def say_hi():
    print("Hello World")


def add(x, y):
    result = x + y
    print(f"{x} + {y} = {result}")


def add2(x, y, z):
    result = x + y + z
    print(f"{x} + {y} + {z} = {result}")


def add3(x, y):
    result = x + y
    print(f"{x} + {y} = {result}")
    return result


add(1, 2)
add2(1, 2, 3)
r = add3(1, 2)
print(f"add3's ans is {r}")
