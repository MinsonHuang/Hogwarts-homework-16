# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/10-14:16
# 此模块主要测试列表推导式的使用


def test_listDeduction():
    """
    测试列表推导式；
    把列表的与项，变成项的平方
    :return:
    """
    listTwo = [n ** 2 for n in range(1, 10)]
    print(listTwo)


# 测试列表推导式
def test_listDeduction2():
    listOne = [1, 2, 3, 4, 5, 6]
    listTwo = [i+1 for i in listOne]
    print("listOne", listOne)
    print("listTwo", listTwo)


# 测试复杂的列表推导式， 带有条件判断的列表推导式
def test_listDeduction():
    listOne = [i for i in range(1, 10)]
    print("listOne", listOne)
    listTwo = [i for i in listOne if i % 2 == 0]
    print("listTwo", listTwo)
    # range(1,10) 返回的 是一个<class 'range'> 类的数据
    print(type(range(1, 10)))


# 测试嵌套列表推导式
def test_nestingListDudection():
    listOne = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
    print("listOne:", listOne)
    # 嵌套列表推导式，先写外层的列表推导式，再写内层的列表推导式，
    # 这样可以遍历嵌套列表的所有数据
    listTwo = [i for l in listOne for i in l if i % 2 == 0]
    print("listTwo:", listTwo)


# 测试列表推导式，在外层在判断，然后内层也做判断
def test_nestingListDeduction():
    listOne = [[1, 2, 3], [7, 8, 9], [10], [6]]
    print("listOne:", listOne)
    # 嵌套列表推导式，外层和内层都有条件判断，进行多层数据过滤
    listTwo = [i**2 for l in listOne if len(l) > 1 for i in l if i % 2 == 1]
    print("listTwo:", listTwo)

