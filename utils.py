"""
常用工具的封装
"""
import xlrd
import xlwt
import openpyxl
import os
import json


def get_config(key):
    with open("./config.json") as f:
        conf = json.load(f)
    return conf[key]


# def write_header(worksheet):
#     header = ["测试案例路径", "测试案例名称", "测试案例描述",
#               "计划执行时长(分钟)", "步骤描述", "预期结果", "优先级", "测试模块", "执行方式", "测试类型"]
#
#     for n, i in enumerate(header):
#         worksheet.write(0, n, i)
#         n += 1


# def write_data(worksheet, testcases):
#     row = 1
#     for tc in testcases:
#         wl = tc.toList()
#         for l in wl:
#             for i, j in enumerate(l):
#                 worksheet.write(row, i, j)
#             row += 1
# 

# def generate_excel(testcases, p):
#     """将testcase列表转换成excel文件
#     """
#     workbook = xlwt.Workbook(encoding='utf-8')
#     worksheet = workbook.add_sheet('My Worksheet')
#     write_header(worksheet)
#     write_data(worksheet, testcases)
#     filename = os.path.abspath(p).rpartition(".")[0]+".xlsx"
#     workbook.save(filename)


def write_header(worksheet):
    header = ["测试案例路径", "测试案例名称", "测试案例描述",
              "计划执行时长(分钟)", "步骤描述", "预期结果", "优先级", "测试模块", "执行方式", "测试类型"]
    worksheet.append(header)


def write_data(worksheet, testcases):
    for tc in testcases:
        wl = tc.toList()
        for l in wl :
            worksheet.append(l)


def generate_excel(testcases, p):
    """将testcase列表转换成excel文件,使用openpyxl模块
    """
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    write_header(worksheet)
    write_data(worksheet, testcases)
    filename = os.path.abspath(p).rpartition(".")[0]+".xlsx"
    workbook.save(filename)
