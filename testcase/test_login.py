'''
===================
姓名：半明媚。
Time：2023/8/1 0001  上午 0:58
Email:630906365@qq.com
====================
'''

import unittest
from common.handle_excel import Excel
from common.handle_path import DATA_DIR
import os
from unittestreport import ddt, list_data
import requests
from common.handle_conf import conf
from common.handle_log import log
from tools.create_phone import random_phone


@ddt
class TestLogin(unittest.TestCase):
    """测试登录"""
    excel = Excel(os.path.join(DATA_DIR, "cases_data.xlsx"), "login").read_data()
    # print(excel)

    @list_data(excel)
    def test_login(self, item):
        # 准备测试数据
        expected = eval(item["expected"])
        param = eval(item["data"])
        if param["mobile_phone"]=="#phone#":
            param["mobile_phone"]=random_phone()
            print(param["mobile_phone"])
        url = conf.get("env","base_url") +  item["url"]
        method = item["method"]
        # print(method)
        headers = {
            "X-Lemonban-Media-Type": "lemonban.v2"
        }
        # 请求接口
        response = requests.request(url=url, method=method, headers=headers, json=param)
        # 获取结果并断言
        res = response.json()
        print("expected====",expected)
        print("res=====",res)
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])

        except AssertionError as e:
            log.error("用例---{}---执行不通过".format(item["title"]))
            print(e)
            raise e
        else:
            log.info("用例---{}---执行通过".format(item["title"]))




if __name__ == '__main__':
    unittest.main()