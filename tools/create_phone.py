'''
===================
姓名：半明媚。
Time：2023/8/6 0006  上午 0:17
Email:630906365@qq.com
====================
'''

import random
from common.handle_db import db


def random_phone():
    """随机生成一个未注册的手机号"""
    num = "131"
    for i in range(8):
        num = num + str(random.randint(0, 9))
    sql = "SELECT * FROM future.member where mobile_phone={}".format(num)
    res = db.find_data(sql)
    if not res:
        return num


if __name__ == '__main__':
    print(random_phone())
