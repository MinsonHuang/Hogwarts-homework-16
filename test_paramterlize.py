# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/9-20:34
import pytest


def add_function(a, b):
    return a + b


@pytest.mark.parametrize("a,b,expected", [
    (3,5,8),
    (-1,-2,-3),
    (1000,1000,2000)],
    # inds
)
def test_add(a, b, expected):
    assert add_function(a, b) == expected


@pytest.mark.parametrize("a",[0,1])
@pytest.mark.parametrize("b",[7,8])
def test_func_b(a, b):
    """参数组合测试"""
    print("a:%s,b:%s"%(a,b))
