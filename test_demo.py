# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/9-20:34


def test_one():
    a = 5
    b = 1
    assert a != b
    print("这是我的第n个pytest测试用例")


class TestDemo:
    def test_two(self):
        a = 5
        b = 1
        assert a != b
        print("这是我的第n个在class中的pytest测试用例")