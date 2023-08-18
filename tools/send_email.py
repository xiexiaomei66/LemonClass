'''
===================
姓名：半明媚。
Time：2023/8/18 0018  下午 15:29
Email:630906365@qq.com
====================
'''
"""
QQ邮箱的服务器地址是smtp.qq.com 端口号465
163邮箱 smtp.163.com 端口号465
#发送邮箱服务器
smtpserver='smtp.163.com'
#发送邮件用户名密码 授权密码JWMEKBMHVQTILQBE
user='xie_xiao_mei@163.com'
password='1231XXM69'#授权码，可以在邮箱设置，不是登录密码
#发送和接收邮件的邮箱
sender='xie_xiao_mei@163.com'
receive='630906365@qq.com'
QQ
"""

from unittestreport import TestRunner
import unittest
from unittestreport import TestRunner
import os
from common.handle_path import CASE_DIR,REPORT_DIR
import time

suite=unittest.defaultTestLoader.discover(os.path.join(CASE_DIR))
time_mat=time.strftime("%Y%m%d",time.localtime())
runner=TestRunner(suite, filename="{}report1.html".format(time_mat),
                 report_dir=REPORT_DIR,
                 title='接口自动化测试报告',
                 tester='谢小妹',
                 desc="前程贷项目测试生产的报告",
                 templates=1)
# runner.run()
#重跑机制
runner.rerun_run(count=2,interval=2)

runner.send_email(host="smtp.163.com",
                  port=465,
                  user="xie_xiao_mei@163.com",
                  password="JWMEKBMHVQTILQBE",
                  to_addrs=["630906365@qq.com","xie_xiao_mei@163.com"],
                  is_file=True)