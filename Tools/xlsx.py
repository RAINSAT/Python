# -*- coding:utf8 -*-

import xlwt
import xlrd

class Xlsx(object):
	"""
	读取 xlsx
	写入 xlsx
	"""
	@staticmethod
	def read_xlsx():
		pass

    # @staticmethod
	# def write_xlsx(xlsx_name,sheet_name,content):
	# 	# 创建工作簿
	# 	workbook = xlwt.Workbook(encoding="ascii")
    #     worksheet = workbook.add_sheet(sheet_name)
    #     i = 0
    #     for fan in content:
    #         part = str(fan).rsplit("\\",1)
    #         worksheet.write(i, 0, label = part[0])
    #         worksheet.write(i,1,label = part[1])
    #         i = i + 1
    #     workbook.save(xlsx_name)

if __name__ == '__main__':
	x = Xlsx("f:/test.xlsx")
		