'''
===================
姓名：半明媚。
Time：2023/8/2 0002  上午 0:07
Email:630906365@qq.com
====================
'''
import unittest
import os
from common.handle_excel import Excel
from common.handle_path import DATA_DIR
from common.handle_log import log
from unittestreport import ddt, list_data
import requests
from common.handle_conf import conf
from tools.create_phone import random_phone
from common.handle_db import db


@ddt
class TestRegister(unittest.TestCase):
    """测试注册接口"""
    excel = Excel(os.path.join(DATA_DIR, "cases_data.xlsx"), "register").read_data()

    @list_data(excel)
    def test_register(self, case):
        # 准备数据
        expected = eval(case["expected"])

        # ----------注册号码处理方式一 start-----------------------
        # if "#phone#" in case["data"]:
        #     phone=random_phone()
        #     case["data"]=case["data"].replace("#phone#",phone)
        # param = eval(case["data"])
        # print(param["mobile_phone"])
        # ----------------end-------------------------------------

        # ----------注册号码处理方式二 start-------------------------
        param = eval(case["data"])
        if param["mobile_phone"] == "#phone#":
            param["mobile_phone"] = random_phone()
        # print(param["mobile_phone"])
        # ----------------end-------------------------------------

        url = conf.get("env", "base_url") + case["url"]
        method = case["method"]
        # 这里要注意，从conf文件取出来的是str带有双引号r，但是headers不需要传双引号
        headers = eval(conf.get("env", "headers"))
        # 请求接口
        response = requests.request(url=url, method=method, headers=headers, json=param)
        # 断言
        res = response.json()
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])
            # 查询数据库校验
            sql=case["sql"]
            if sql:
                res =db.find_data(sql.format(param["mobile_phone"]))
                self.assertTrue(res)

            log.info("用例---{}---执行通过".format(case["title"]))
        except AssertionError as e:
            log.error("用例---{}---执行失败".format(case["title"]))
            raise e


if __name__ == '__main__':
    TestRegister.test_register()
