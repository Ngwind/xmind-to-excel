"""
命令行入口
"""
import xmind
import sys
from parsers import get_testcases
from utils import generate_excel


if __name__ == "__main__":
    if len(sys.argv) == 2:
        sh = xmind.load(sys.argv[1])
        rt = sh.getPrimarySheet().getRootTopic()
        testcase_list = get_testcases(rt, rt.getTitle())
        generate_excel(testcase_list, sys.argv[1])
        
    else:
        raise Exception("argv is not 2")
