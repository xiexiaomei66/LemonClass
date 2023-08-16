'''
===================
姓名：半明媚。
Time：2023/8/6 0006  下午 23:35
Email:630906365@qq.com
====================
'''
import requests
from common.handle_conf import conf

def login(mobile,pwd):
    url=conf.get("env","base_url")+"/member/login"
    data={
        "mobile_phone": mobile,
        "pwd": pwd
    }
    headers=eval(conf.get("env","headers"))
    response = requests.post(url=url,json=data,headers=headers)
    res=response.json()
    return res


if __name__ == '__main__':
    from jsonpath import jsonpath
    res=login()
    token=jsonpath(res,"$..token")
    id=jsonpath(res,"$..id")
    print(token)
    print(id)
