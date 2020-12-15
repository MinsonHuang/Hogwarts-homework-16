# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/13-14:13
import pytest


class Test_Demo():
    @pytest.mark.demo
    def test_demo(self):
        print("demo用例")

    @pytest.mark.smoke
    @pytest.mark.demo
    def test_two(self):
        print("smoke测试用例")


