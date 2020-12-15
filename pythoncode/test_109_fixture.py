# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/13-15:22
import pytest


@pytest.fixture()
def fixture_one():
    print("执行我myfixture")


class Test_Demo:
    def test_one(self, fixture_one):
        print("执行test_one")
        assert 1 + 1 == 2

    def test_two(self, fixture_one):
        print("执行test_two")
        assert 1 + 1 == 2

    def test_three(self):
        print("执行test_three")
        assert 1 + 1 == 2

    def test_four(self, fixture_one):
        print("执行test_four")
        assert 1 + 1 == 2
