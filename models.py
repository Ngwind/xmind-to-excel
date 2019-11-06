"""
测试用例的模型
"""
from typing import List, Optional
from xmind.core.topic import TopicElement


class TestCase(object):

    def __init__(self, testSuite: str, topicElement: TopicElement, desc="", execTime="", module="", execType="手工", testType="WEB测试"):
        self.testSuite = testSuite
        self.topicElement = topicElement
        self.testName = topicElement.getTitle()
        self.desc = desc
        self.execTime = exec
        self.module = module
        self.execType = execType
        self.testType = testType

    def __str__(self):
        r = [self.testSuite, self.testName, self.desc, self.execTime, self.testStep,
             self.priority, self.module, self.execType, self.testType]
        return str(r)

    @property
    def priority(self):
        marker = [i.getMarkerId().name for i in self.topicElement.getMarkers()]
        if "priority-1" in marker:
            p = "高"
        elif "priority-2" in marker:
            p = "中"
        elif "priority-3" in marker:
            p = "低"
        else:
            raise Exception("no usefull marker in :"+self.testName)
        return p

    @property
    def testStep(self):
        ts_list = []
        for i in self.topicElement.getSubTopics():
            for j in i.getSubTopics():
                ts_list.append([i.getTitle(), j[0].getTitle()])
        return ts_list
