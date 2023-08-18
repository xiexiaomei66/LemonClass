'''
===================
姓名：半明媚。
Time：2023/8/6 0006  下午 23:35
Email:630906365@qq.com
====================
'''
import requests
from jsonpath import jsonpath
from common.handle_conf import conf
from tools.create_phone import random_phone


class InitEnvData:
    """环境初始化"""

    def register(self, mobile_conf, pwd_conf, type=1):
        """
        注册后将账号密码存入config文件以备只需
        :param mobile_conf:存入配置文件里面的mobile名称
        :param pwd_conf:存入配置文件里面的密码
        """
        # 从配置文件获取url
        url = conf.get("env", "base_url") + "/member/register"
        # 生成一个数据库不存在的手机号码注册
        mobile_phone = random_phone()
        pwd = "xiexiaomei123"
        data = {
            "mobile_phone": mobile_phone,
            "pwd": pwd,
            "type": type
        }
        headers = eval(conf.get("env", "headers"))
        response = requests.post(url=url, json=data, headers=headers)
        res = response.json()
        # 注册成功后将账号密码存入config文件
        if res["code"] == 0:
            conf.write_conf("data", mobile_conf, mobile_phone)
            conf.write_conf("data", pwd_conf, pwd)
        #将写入conf文件的值传出去
        return mobile_phone, pwd

    def login(self, mobile, pwd):
        """登录，获取token，member_id
        :param mobile：登录账号
        :param pwd :登录密码
        """
        url = conf.get("env", "base_url") + "/member/login"
        data = {
            "mobile_phone": mobile,
            "pwd": pwd
        }
        headers = eval(conf.get("env", "headers"))
        response = requests.post(url=url, json=data, headers=headers)
        res = response.json()
        token = "Bearer" + " " + jsonpath(res, "$..token")[0]
        member_id = jsonpath(res, "$..id")[0]
        # print("")
        return token, member_id

    def recharge(self, token,member_id, amount=500000):
        """
        :param member_id:用户id
        :param token：token
        :param amount：充值金额，默认充值50万

        """
        url = conf.get("env", "base_url") + "/member/recharge"
        data = {
            "member_id": member_id,
            "amount": amount
        }
        headers = eval(conf.get("env", "headers"))
        headers["Authorization"] = token
        response = requests.post(url=url, json=data, headers=headers)
        res = response.json()

    def init_env_data(self):
        """注册，登录，充值初始化"""
        # 注册投资人
        user_invest = InitEnvData().register(mobile_conf="mobile_invest", pwd_conf="pwd_invest")
        # 注册借款人
        user_borrow = InitEnvData().register(mobile_conf="mobile_borrow", pwd_conf="pwd_borrow")
        # 注册管理员
        user_admin = InitEnvData().register(mobile_conf="mobile_admin", pwd_conf="pwd_admin", type=0)
        # 获取token和member_id
        token_borrow, member_id_borrow = InitEnvData().login(*user_borrow)
        token_invest,member_id_invest=InitEnvData().login(*user_invest)
        #充值
        InitEnvData().recharge(token_borrow,member_id_borrow)
        InitEnvData().recharge(token_invest,member_id_invest)


if __name__ == '__main__':

    res1=InitEnvData().register("mobile_invest","pwd_invest")
    print(res1)
    res2=InitEnvData().login(*res1)
    # print(type(res2))

    # InitEnvData().init_env_data()


