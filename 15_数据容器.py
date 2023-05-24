# Chlorine 
# Time : 2022/11/10 16:27

"""
    1. 数据容器入门：
        1. 数据容器中一次性可以存放多个数据
        2. 目的是去批量存储多份数据数据，并且每个数据元素的类型都是任意的
        3. Py中的数据容器：
            特点：
                1. 元素是否可重复
                2. 是否可以修改
                3. 是否有序
                etc.
            分类：
                1. List 列表
                2. tuple 元组
                3. str 字符串
                4. dict 字典

    2. List 列表
        1. List 列表的定义
            1. 字面量：
                [元素1，元素2，...]
            2. 变量：
                val = [元素1，元素2，...]
            3. 定义空列表：
                val = []
                val = list()
        2. 列表可以作为一个整体进行输出
        3. 列表中存储的数据类型，是任意的，可以不是一致的
        4. 列表中还可以再存入列表（嵌套）
        5. 列表的下标索引：
            1. 使用列表的下标索引来取出对应位置的索引
            2. 下标从0开始
            3. name_list = ["123", "234", "Hello World"]

               name_lit[0] = "123"
               name_lit[1] = "234"

               name_list[-1] = "Hello World"
               name_list[-2] = "234"
               name_list[-3] = "123"
            4. 嵌套列表的下标也是嵌套定义的
            5. 下标不可以超出列表的索引范围，否则会无法取出，同时也会发生报错
        6. 列表的常用操作：
            1. 列表插入元素
                列表.insert(下标, 元素)
                再指定的下标位置，插入指定的元素
            2. 删除元素
            3. 清空列表
            4. 修改元素
            5. 统计元素个数
            6. 查询功能
                列表对象.index(元素)
                如果列表有这个元素，就会返回这个元素的下标
                如果列表没有这个元素，就会报错
            7. 追加元素
                列表.append(元素)
                元素的插入的结果一定是在列表的尾部的，所以不需要去指定插入的位置

                列表.extend(容器)
                可以将其他的数据容器的内容全部取出，依次追加到列表的尾部

"""

name_list = ["123", "234", "Hello World"]
print(list)

print(name_list[0])
print(name_list[1])
print(name_list[2])

print(name_list[-1])
print(name_list[-2])
print(name_list[-3])

List = [[1, 2, 3], [3, 4, 5]]
print(List[0][0])
print(List[0][1])
print(List[0][2])

print(List[1][0])
print(List[1][1])
print(List[1][2])

str = "123"
print(f"\"123\" is located at {name_list.index(str)}")
# print(name_list.index(123))

name_list[0] = "This data is changed"
print(name_list)

name_list.insert(0, "a data is inserted at label 0")
print(name_list)

name_list.append("a data is appended to the List")
print(name_list)

my_dict = {"CL": 99, "LJJ": 100}
my_dict["YH"] = 20
print(my_dict)
my_dict["YH"] = 30
print(my_dict)


