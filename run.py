'''
===================
姓名：半明媚。
Time：2023/8/1 0001  上午 1:21
Email:630906365@qq.com
====================
'''
import unittest
from unittestreport import TestRunner
import os
from common.handle_path import CASE_DIR,REPORT_DIR
import time

suite=unittest.defaultTestLoader.discover(os.path.join(CASE_DIR))
time_mat=time.strftime("%Y%m%d",time.localtime())
runner=TestRunner(suite, filename="{}report1.html".format(time_mat),
                 report_dir=REPORT_DIR,
                 title='测试报告',
                 tester='谢小妹',
                 desc="前程贷项目测试生产的报告",
                 templates=1)
runner.run()
#这是我在本地添加的
