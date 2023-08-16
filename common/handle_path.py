'''
===================
姓名：半明媚。
Time：2023/7/31 0031  下午 23:34
Email:630906365@qq.com
====================
'''
import os

# 获取工程路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试数据路径
DATA_DIR = os.path.join(BASE_DIR, 'data')
#报告路径
REPORT_DIR=os.path.join(BASE_DIR,'reports')
#日志路径
LOG_DIR=os.path.join(BASE_DIR,'log')
#配置文件路径
CONF_DIR=os.path.join(BASE_DIR,'conf')
#用例路径
CASE_DIR=os.path.join(BASE_DIR,'testcase')
# print(CONF_DIR)
# print(os.path.join(DATA_DIR,"cases_data.xlsx"))