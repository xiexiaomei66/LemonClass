'''
===================
姓名：半明媚。
Time：2023/8/18 0018  上午 0:37
Email:630906365@qq.com
====================
'''
import pytest
import os

#encoding=utf-8

# pytest.main(['--alluredir=allure-results'])
pytest.main(["--alluredir=reports"])
# os.system('allure-report')
os.system('allure serve reports')

