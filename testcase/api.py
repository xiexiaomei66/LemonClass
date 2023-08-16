'''
===================
姓名：半明媚。
Time：2023/7/29 0029  下午 15:49
Email:630906365@qq.com
====================
'''
import requests
from jsonpath import jsonpath

url = 'http://api.lemonban.com/futureloan/member/login'
param = {
    "mobile_phone": "13888888888",
    "pwd": "12345678"
}
headers = {
    "X-Lemonban-Media-Type": "lemonban.v2"

}


url2='http://api.lemonban.com/futureloan/member/register'
response = requests.post(url=url, json=param,headers=headers)
res=response.json()
# print(res)
print(type(res["data"]["token_info"]["token"]))
print("通过jsonpath获取的token",jsonpath(res,"$..token")[0])