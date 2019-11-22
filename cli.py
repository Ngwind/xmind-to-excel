"""
命令行入口
"""
import xmind
import sys
from parsers import get_testcases
from utils import generate_excel, get_config


if __name__ == "__main__":
    if len(sys.argv) == 2:
        sh = xmind.load(sys.argv[1])
        rt = sh.getPrimarySheet().getRootTopic()
        default_prefix = get_config("default_prefix")
        testcase_list = get_testcases(rt, default_prefix + rt.getTitle())
        generate_excel(testcase_list, sys.argv[1])
    else:
        raise Exception("argv is not 2")
