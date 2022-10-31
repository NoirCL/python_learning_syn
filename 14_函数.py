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
