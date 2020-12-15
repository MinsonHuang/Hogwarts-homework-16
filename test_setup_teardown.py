# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/9-21:02
import pytest

def setup_module():
    print("setup_module: 整个测试模块的测试用例开始前，执行的初始化动作，整个只执行一次")

def teardown_module():
    print()



def setup_function():
    print("setup_function 每个非类中的测试用例开始前，都会执行的初始化动作")


def teardown_function():
    print("teardown_function 每个非类中的测试用例执行后，都会执行的释放资源动作")


def test_function_three():
    print("执行了非类中的测试用例test_function_three")


def test_function_four():
    print("执行了非类中的测试用例test_function_four")


class TestClass:
    def setup_class(self):
        print("setup_class 每个类中所有用例开始前执行的初始化动作")

    def teardown_class(self):
        print("teardown_class 每个没中所有用例结束后执行的释放资源动作")

    def setup_method(self):
        print("setup_method 每个用例开始执行前的初始化操作")

    def teardown_method(self):
        print("teardown_method 每个用例结束的时候执行的释放资源操作")



    def test_one(self):
        print("执行了test_one用例")

    def test_two(self):
        print("中性了test_two用例")