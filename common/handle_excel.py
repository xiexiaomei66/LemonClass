'''
===================
姓名：半明媚。
Time：2023/7/21 0021  上午 0:30
Email:630906365@qq.com
====================
'''

import openpyxl


class Excel:
    """处理Excel"""

    def __init__(self, filename, sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def open(self):
        # 创建工作簿对象
        self.wb = openpyxl.load_workbook(self.filename)
        # 打开s表单
        self.sh = self.wb[self.sheetname]

    def read_data(self):
        """读取excel"""
        self.open()

        # 读取所有单元格并转换成列表
        res = list(self.sh.rows)
        # 读取第一行数据并将数据放入title
        title = []
        for c in res[0]:
            title.append(c.value)
        data_case = []
        for item in res[1:]:
            data = []
            for c in item:
                data.append(c.value)
            data_case.append(dict(zip(title, data)))
        return data_case

    def write_data(self, row, column, value):
        self.open()
        self.sh.cell(row=row, column=column, value=value)
        self.wb.save(self.filename)


if __name__ == '__main__':
    excel = Excel(r'F:\lemon_Class_API\casedata\cases_data.xlsx', 'login')
    print(excel.read_data())