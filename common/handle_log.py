'''
===================
姓名：半明媚。
Time：2023/8/1 0001  上午 0:08
Email:630906365@qq.com
====================
'''
import logging
from logging.handlers import TimedRotatingFileHandler
import os
from common.handle_path import LOG_DIR
import time




def log():
    # 创建一个日志收集器
    log = logging.getLogger("xiaomei.xie")
    # 设置日志收集器等级
    log.setLevel("DEBUG")
    # 输出到控制台
    ch = logging.StreamHandler()
    # 设置等级
    ch.setLevel("DEBUG")
    # 输出到文件并日志轮转
    time_mat=time.strftime("%Y%m%d",time.localtime())
    fh = TimedRotatingFileHandler(os.path.join(LOG_DIR,'{}log.log'.format(time_mat)),
                                      when='midnight',
                                      interval=1,
                                      backupCount=7,
                                      encoding='utf-8')
    # 设置等级
    fh.setLevel("DEBUG")
    # 加载输出流
    log.addHandler(ch)
    log.addHandler(fh)
    #设置输出格式
    formats = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
    mat = logging.Formatter(formats)
    #将格式绑定输出渠道
    ch.setFormatter(mat)
    fh.setFormatter(mat)
    # print("dddd")
    return log

log=log()
