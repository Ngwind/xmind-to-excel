"""
将xmind解析成excel
"""
import models
from xmind.core.topic import TopicElement
from models import TestCase


def get_testcases(topics: TopicElement, prefix=""):
    """递归函数
    用于遍历一个topic下的所有topic，
    如果有marker，就停止递归。
    """
    tl = []
    for t in topics.getSubTopics():
        if t.getMarkers():
            # t是测试用例
            tc = TestCase(prefix,t)
            tl.append(tc)
        else:
            tl += get_testcases(t, prefix+"\\"+t.getTitle())
    return tl

