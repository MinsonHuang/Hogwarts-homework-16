# coding=utf-8
# 作者    ：  MinsonHuang
# 创建时间 :  2020/12/10-16:45


# 测试python的注释符号
# 字符串中的#号，是不会被当做注释符号的
def test_explain_character():
    print("#123#567")


# 非字符串、空白出、行尾的#会被当做注释符号，不会被python解析器执行
def test_explain_character_2():
    print("123#")
    # 下面的print语句不会被python解析器执行，因为Python解析器把它当做注释
    #print("222")