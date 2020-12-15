# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/13-15:15
import yaml


def step1():
    print("step1")


def step3():
    print("step2")


def step3():
    print("step3")


def steps(path):
    with open(path) as file:
        steps = yaml.safe_load(file)
        for step in steps:
            pass

