# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/13-15:32
import pytest


@pytest.fixture()
def fixture_one():
    print("执行我fixture_one")


@pytest.fixture(params=["参数1","参数2"])
def fixture_two(request):
    print("执行了fixture_two")
    print(request.param)


@pytest.fixture(params=[{"userName": "zhangsna", "userAge": 23}, {"userName": "lisi", "userAge": 24}])
def fixture_three(request):
    print("执行了fixture_three")
    print(request.param["userName"])


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')