# Chlorine 
# Time : 2022/10/28 16:09

"""
    1. 数据是有类型的
        主要接触三类数据类型：
            1. 整数 int
            2. 浮点数 float
            3. 字符串 string (str)
    2. 查看数据类型
        type(被查看类型的数据)
        type() 可以查看字面值的数据类型，也可也查看变量中的值的数据类型
    3. 用变量才存储type()的返回结果
        int_type = type(123)
    4. py中的变量实际上是没有类型的，实际上查看的是变量中的数据的类型，变量只是盒子
"""

print(type(123))
print(type(123.123))
print(type("123"))

int_type = type(123)
print(int_type)

a = 123.123
float_type = type(a)
print(int_type)
