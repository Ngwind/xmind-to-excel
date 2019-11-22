"""
测试用例的模型
"""
from typing import List, Optional
from xmind.core.topic import TopicElement
from utils import  get_config


class TestCase(object):

    def __init__(self, testSuite: str, topicElement: TopicElement, desc="", execTime="", module="", execType="", testType=""):
        self.testSuite = testSuite
        self.topicElement = topicElement
        self.testName = topicElement.getTitle()
        self.desc = desc
        self.execTime = execTime
        self.module = module
        self.execType = get_config("default_execType")
        self.testType = get_config("default_testType")

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
            p = ""
        return p

    @property
    def testStep(self):
        ts_list = []
        for i in self.topicElement.getSubTopics():
            if i.getSubTopics() is None:
                ts_list.append([i.getTitle(), ''])
            for j in i.getSubTopics():
                ts_list.append([i.getTitle(), j.getTitle()])
        return ts_list

    def toList(self):
        rel = []
        l = len(self.testStep)
        if l == 0:
            rel.append([self.testSuite, self.testName, self.desc, self.execTime,
                        "", "", self.priority, self.module, self.execType, self.testType])
        else:
            for i, ts in enumerate(self.testStep):
                if i == 0:
                    rel.append([self.testSuite, self.testName, self.desc, self.execTime, ts[0],
                                ts[1], self.priority, self.module, self.execType, self.testType])
                else:
                    rel.append(["", "", "", "", ts[0],
                                ts[1], "", "", "", ""])

        return rel
