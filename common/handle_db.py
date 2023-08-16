'''
===================
姓名：半明媚。
Time：2023/8/5 0005  下午 23:43
Email:630906365@qq.com
====================
'''
import pymysql
from common.handle_conf import conf


class DB:
    def __init__(self):
        # 1、创建连接对象
        self.con = pymysql.connect(host=conf.get("db", "host"),
                                   user=conf.get("db", "user"),
                                   password=conf.get("db", "password"),
                                   charset='utf8',
                                   # 设置游标返回的数据类型为列表嵌套字典，不设置则默认是元组
                                   cursorclass=pymysql.cursors.DictCursor,
                                   # database=conf.get("db",""),
                                   # 因为涉及到可能有多个数据库，所以这里不要写死，后面写SQL时候带上数据库比较灵活
                                   port=3306)
         # 创建一个游标
        self.cur = self.con.cursor()



    def find_data(self, sql):
        #先提交事务，同步数据库最新状态
        self.con.commit()
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res



db = DB()
if __name__ == '__main__':
    from decimal import Decimal
    # 3、执行sql
    sql = "SELECT leave_amount FROM future.member where id=127634"
    res =db.find_data(sql)[0]["leave_amount"]+100

    print(type(res))
