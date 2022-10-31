# Chlorine 
# Time : 2022/10/29 15:36

"""
    1. 字符串的三种定义方式：
        1. 单引号定义法
            name = 'Hello World'
        2. 双引号定义法
            name = "Hello World"
        3. 三引号定义法
            和多行注释的写法一样，同样可以支持换行的操作
            如果使用变量去接收多行注释，多行注释就会变成一个字符串，否则就仍然是一个多行注释

    2. 如果定义的字符串包含双引号本身
        1. 单引号定义法，内部可以使用双引号
        2. 双引号定义法，内部可以包含单引号
        3. 使用转意字符 \\，可以让特殊字符失去特殊含义

    3. 字符串的拼接：
        使用加号就可以将两个字符串拼接为一个字符串（一般用来将变量和字面量进行拼接）
            注意：必须是两个字符串，字符串无法直接用加号和其他类型的变量进行拼接

    4. 字符串格式化：
        name = "world"
        message = "hello %s" % name
        message = “hello %s %s %s" % (name, name, name)

        1. %s 是一个固定的占位符号
        2. " " 中的 % 表示占位
        3. s表示将变量变成字符串放入占位的地方
            变量可以为数字, 数字变量被自动转换为了字符串
        4. 多个变量占位，需要在 " " 后的 % 后用括号进行包括，且顺序有严格要求
        5. 其他类似的占位符号：
            %d：将内容转换为整数，放到占位的地方
            %f：将内容转换为浮点数，放到占位的地方
            %s：将内容转换为字符串，放到占位的地方

    5. 格式化的精度控制：
        使用辅助符号m.n来控制数据的宽度和精度
        m：控制宽度，要求是数字，设置的宽度如果小于数字自身，不生效
        n：控制小数点的精度，要求是数字，会进行小数的四舍五入

        %5d：表示数字的宽度为5，如果为11，就是   11
        %7.2f：如果数字为11.345，结果是  11.35
        %.2f：表示不限制宽度，只设置小数点的位数为2

    6. 字符串的格式化方式2
        f "内容{变量} {变量} {变量}"
        这种方式，不需要做精度控制，也不关心类型

    7. 对表达式进行格式化：
        表达式：一条具有明确执行结果的代码语句
            1 + 1，5 * 2 都是表达式，而且都有具体的结果
            name = "张三"，age = 11 也都可以认为是表达式
        "%d" % (1 * 1) 这种写法是不会存储数据的（局部变量）
"""

###
name = 'Hello World'
print(name)

name = "Hello World"
print(name)

name = """Hello World"""
print(name)

name = '"Hello World"'
print(name)

name = "\"Hello World\""
print(name)
###

###
print("Hello " + "World")

name = "World"
print("Hello " + name)
###

###
name = "world"
message = "Hello %s" % name
print(message)

class_num = 57
avg_salary = 16781

message = "%s %s" % (class_num, avg_salary)
print(message)

name = "Hello"
age = 27
price = 17.8
message = "%s %d %f" % (name, age, price)
print(message)
###

###
num1 = 11
num2 = 11.345
print("%5d" % num1)
print("%-5d" % num1)
print("%7.2f" % num2)
print("%.2f" % num2)
###

###
name = "Hello"
num1 = 11
num2 = 11.34
a = f"{name} {num1} {num2}"
print(a)

print("%d" % (1 * 1))
print(f"{1 * 1}")
print("%s" % (type(name)))
###
