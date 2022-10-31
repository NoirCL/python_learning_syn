# Chlorine 
# Time : 2022/10/28 22:07

"""
    1. 目的：
        比如，从文件中读取的数据，其类型默认是字符串，需要人为将其转换为数字类型
    2. 方法：
        1. int(x) 将x转换为整数
        2. float(x) 将x转换为浮点数
        3. str(x) 将对象x转换为字符串
        这三个语句都是通过返回指将转换后的结果返回的
    3. 规则：
        1. 任何类型都可以变成字符串类型（任何被双引号括起来的部分就都是字符串）
        2. 只有数值字符串可以被转换为数字
        3. 浮点数转换为整数，会导致小数点后面的内容全部截断
"""

a = 123
a = str(a)
print(type(a))  # 将整数类型的a转换为字符串类型

float_str = str(12.13)
print(type(float_str), float_str)

# 只要是被双引号引起来的部分就都是字符串
number = int("11")
print(type(number), number)

float_num = float("11.34")
print(type(float_str), float_str)

# 错误实例，字符串变成数字，必须要求字符串内的值全为数字
# num3 = int("Hello World")
# print(type(num3))

float_num = float(11)
print(type(float_num), float_num)

int_num = int(11.34)
print(type(int_num), int_num)


