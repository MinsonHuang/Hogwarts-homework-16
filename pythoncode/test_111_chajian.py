# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/13-15:48
import pytest


@pytest.mark.run(order=3)
def test_one():
    print("one")


@pytest.mark.run(order=1)
def test_two():
    print("two")


@pytest.mark.run(order=2)
def test_three():
    print("three")




