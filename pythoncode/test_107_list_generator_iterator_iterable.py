# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/10-21:45
import sys


def test_list():
    listOne = [1, 2, 3, 4, 5]
    print(sys.getsizeof(listOne))


# 测试用列表生成式，用一个list生成另外一个list
# 把列表中的大写字母，转换为小写字符，数字不变
# 通过lambda函数形式实现，即匿名函数实现
def test_list_deduction():
    listOne = ["ZhangSan", "Lisi", "WangWu", "123", "AA"]
    listTwo = [item.lower() if isinstance(item, str) else item for item in listOne]
    print("listTwo:", listTwo)


# 测试用map，根据一个list生成另外一个list
def test_map_function():
    listOne = ["ZhangSan", "Lisi", "WangWu", "123", "AA"]
    listTwo = map(lambda x: x.lower() if isinstance(x, str) else x, listOne)
    print("listTwo:", listTwo)
    listThree = list(listTwo)
    print("listThree:", listThree)


def lowerFunction(x):
    if isinstance(x, str):
        x = x.lower()
    return x


# 测试用map，根据一个list生成另外一个list
# 把列表中的大写字母，转换为小写字符，数字不变
# 通过函数形式过滤
def test_map_function_2():
    listOne = ["ZhangSan", "Lisi", "WangWu", "123", "AA", 6, 9, 1.5]
    listTwo = map(lowerFunction, listOne)
    print("listTwo:", listTwo)
    listThree = list(listTwo)
    print("listThree:", listThree)


# 测试用map和list结合，用一个list生成另外一个list
# 过滤中列表的字符串，并转换为小写
# 先过滤，后转为小写
def test_map_filter_function_3():
    listOne = ["ZhangSan", "Lisi", "WangWu", 123, "AA", 6, 6.5]
    mapTwo = map(lambda x: x.lower(), filter(lambda x: isinstance(x, str), listOne))
    print("mapTwo:", mapTwo)
    listThree = list(mapTwo)
    print("listOne:", listOne)
    print("listThree:", listThree)


# 测试用类似列表生成式构造生成器
def test_generator_1():
    g1 = (2*i+1 for i in range(3, 6))
    print(type(g1)) # <class 'generator'>
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))  # 已经越界，会报异常StopIteration


# 测试用包含yield的函数来构造生成器
def generator_2():
    for i in range(3, 6):
        yield 2*i+1


def test_generator_2():
    g2 = generator_2()
    print(type(g2))  #<class 'generator'>
    print(next(g2))
    print(next(g2))
    print(next(g2))
    print(next(g2))  # 已经越界，会报异常StopIteration


# 测试用for循环便利生成器
def test_generator3():
    g3 = (2*i+1 for i in range(3, 6))
    for item in g3:
        print(item)


