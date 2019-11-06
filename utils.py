"""
常用工具的封装
"""
import xlrd
import xlwt
import os


def write_header(worksheet):
    header = ["测试案例路径", "测试案例名称", "测试案例描述",
              "计划执行时长(分钟)", "步骤描述", "预期结果", "优先级", "测试模块", "执行方式", "测试类型"]
    n = 0
    for i in header:
        worksheet.write(0, n, i)
        n += 1

def write_data(worksheet,testcases):
    pass


def generate_excel(testcases, p):
    """将testcase列表转换成excel文件
    """
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('My Worksheet')
    write_header(worksheet)
    write_data(worksheet, testcases)
    filename = os.path.abspath(p).rpartition(".")[0]+".xls"
    workbook.save(filename)
