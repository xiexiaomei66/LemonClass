'''
===================
姓名：半明媚。
Time：2023/7/31 0031  下午 23:47
Email:630906365@qq.com
====================
'''

import os
from configparser import ConfigParser
from common.handle_path import CONF_DIR


class Config(ConfigParser):
    def __init__(self, filename, encoding='utf-8'):
        super().__init__()
        self.filename = filename
        self.encoding = encoding
        self.read(filename, encoding=encoding)

    def write_conf(self, section, option, value):
        """写入配置参数"""
        pass
        self.set(section, option, value)
        self.write(fp=open(self.filename, "w", encoding=self.encoding))


# 创建一个配置文件解析器
conf = Config(os.path.join(CONF_DIR, "config.ini"))
