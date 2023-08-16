'''
===================
姓名：半明媚。
Time：2023/8/14 0014  下午 23:43
Email:630906365@qq.com
====================
'''

import re
from common.handle_conf import conf


def replace_data(data, cls):
    """替换用例参数"""
    while re.search("#(.+?)#", data):
        # 需要替换的数据
        item = re.search("#(.+?)#", data)
        rep_data = item.group()
        # 要替换的属性
        key = item.group(1)
        try:
            value = conf.get("test_data", key)
        except:
            value = getattr(cls, key)
        data = data.replace(rep_data, str(value))
        return data
