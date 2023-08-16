'''
===================
姓名：半明媚。
Time：2023/8/6 0006  下午 23:44
Email:630906365@qq.com
====================
'''
import unittest
from unittestreport import ddt, list_data
from common.handle_excel import Excel
from common.handle_path import DATA_DIR
import os
from common.handle_conf import conf
from common.login import login
from jsonpath import jsonpath
import requests
from common.handle_log import log
from common.handle_db import db
from decimal import Decimal


@ddt
class TestRecharge(unittest.TestCase):
    """测试投资接口"""

    @classmethod
    def setUpClass(cls):
        cls.res = login(conf.get("test","mobile_recharge"),conf.get("test","pwd_recharge"))
        cls.token = jsonpath(cls.res, "$..token")[0]
        cls.member_id = jsonpath(cls.res, "$..id")[0]

    excel = Excel(os.path.join(DATA_DIR, "cases_data.xlsx"), "recharge").read_data()

    @list_data(excel)
    def test_recharge(self, case):
        """测试充值接口"""
        # 准备测试数据
        url = conf.get("env", "base_url") + case["url"]
        param = eval(case["data"])
        # 将数据中的member_id替换成当前登录用户的id
        if param["member_id"]=="*member_id*":
            param["member_id"] = self.member_id
        expected = eval(case["expected"])
        method = case["method"]
        headers = eval(conf.get("env", "headers"))
        # 在headers里面加一个鉴权
        headers["Authorization"] = "Bearer " + self.token
        # 请求接口前先查询一次数据库中的余额
        sql = case["sql"]
        if sql:
            s_money = db.find_data(sql.format(self.member_id))[0]["leave_amount"]
            # print(s_money)
        # 请求接口
        response = requests.request(method=method, json=param, headers=headers, url=url)
        res = response.json()
        print("expected====",expected)
        print("res====",res)

        # 断言
        try:
            # 通过接口返回值断言
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])
            # 通过数据库查数据断言
            if sql:
                e_money = db.find_data(sql.format(self.member_id))[0]["leave_amount"]
                self.assertEqual(float(param["amount"]), float(e_money - s_money))
            log.info("用例---{}---执行通过".format(case["title"]))
        except AssertionError as e:
            log.error("用例---{}---执行失败".format(case["title"]))
            raise e


if __name__ == '__main__':
    unittest.main()
