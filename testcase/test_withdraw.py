'''
===================
姓名：半明媚。
Time：2023/8/10 0010  上午 0:00
Email:630906365@qq.com
====================
'''
import os
import unittest
from decimal import Decimal

import requests
from jsonpath import jsonpath
from unittestreport import ddt, list_data

from common.handle_conf import conf
from common.handle_db import db
from common.handle_excel import Excel
from common.handle_log import log
from common.handle_path import DATA_DIR
from tools.init_env import InitEnvData


@ddt
class TestWithdraw(unittest.TestCase):
    """测试提现类"""
    excel = Excel(os.path.join(DATA_DIR, "cases_data.xlsx"), "withdraw").read_data()

    @classmethod
    def setUpClass(cls):
        cls.res = InitEnvData().login(conf.get("test_data", "mobile_withdraw"), conf.get("test_data", "pwd_withdraw"))
        cls.token, cls.member_id = cls.res


    @list_data(excel)
    def test_withdraw(self, case):
        # 准备测试数据
        url = conf.get("env", "base_url") + case["url"]
        param = eval(case["data"])
        param["member_id"] = self.member_id

        expected = eval(case["expected"])
        method = case["method"]
        headers = eval(conf.get("env", "headers"))
        headers["Authorization"] = "Bearer" + " " + self.token
        # 请求接口前查询余额
        sql = case["sql"]
        if sql:
            s_money = Decimal(db.find_data(sql.format(self.member_id))[0]["leave_amount"])

        # if case["title"] == "提现金额大于余额":
        #     sql="SELECT leave_amount FROM future.member where id={}"
        #     s_money = Decimal(db.find_data(sql.format(self.member_id))[0]["leave_amount"])
        #     param["amount"] = s_money + 100


        # 请求接口
        response = requests.request(method=method, url=url, json=param, headers=headers)
        res = response.json()

        print("expected====",expected)
        print("res====",res)

        # 断言
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])
            if sql:
                e_money = Decimal(db.find_data(sql.format(self.member_id))[0]["leave_amount"])
                self.assertEqual(param["amount"], float(s_money - e_money))
                # print(Decimal(s_money - e_money))

            log.info("用例---{}---执行通过".format(case["title"]))
        except AssertionError as e:
            log.error("用例---{}---执行失败".format(case["title"]))
            raise e


if __name__ == '__main__':
    unittest.main()
