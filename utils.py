"""
常用工具的封装
"""
import openpyxl
import os
import json
from prettytable import PrettyTable


def get_config(key):
    with open("./config.json") as f:
        conf = json.load(f)
    return conf[key]


def write_header(worksheet, pt):
    header = ["测试案例路径", "测试案例名称", "测试案例描述",
              "计划执行时长(分钟)", "步骤描述", "预期结果", "优先级", "测试模块", "执行方式", "测试类型"]
    worksheet.append(header)
    pt.field_names = header
    pt.align="l"
    pt.align["优先级"]="c"
    pt.align["执行方式"]="c"
    pt.align["测试类型"]="c"

def write_data(worksheet, testcases, pt):
    for tc in testcases:
        wl = tc.toList()
        for l in wl:
            worksheet.append(l)
            pt.add_row(l)


def generate_excel(testcases, p):
    """将testcase列表转换成excel文件,使用openpyxl模块
    """
    pt = PrettyTable()
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    write_header(worksheet, pt)
    write_data(worksheet, testcases, pt)
    filename = os.path.abspath(p).rpartition(".")[0]+".xlsx"
    workbook.save(filename)
    print(pt)
