# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/11-10:49


def test_list_1():
    listOne = [1, 2, 3]
    print(type(listOne))
    print(list(listOne))


class MyVector:
    def __init__(self, components):
        self.components = components
