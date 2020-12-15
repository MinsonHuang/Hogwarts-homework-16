# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/13-14:55
import pytest
from pythoncode.calculator import Calculator
import yaml


def get_datas():
    with open("./data.yml") as ymlFile:
        yaml.safe_load(ymlFile)
        res = yaml["datas"]
        return []

class TestParam():
    def setup_class(self):
        self.calc = Calculator()

    @pytest.mark.parametrize("a, b, expect", yaml.safe_load(open("./data.yml"))["datas"])
    def test_add(self, a, b, expect):
        assert self.calc.add(a, b) == expect
