#coding:utf-8
#!/usr/bin/env python

def exec():
	try:
		print("code start")
		raise KeyError
	except KeyError as e:
		print('key error')
		return 2
	else:
		print('other error')
	finally:
		print('finally')
		return 4
print(exec())

# 上下文管理器协议
class Sample(object):
	def __init__(self, arg):
		super(Sample, self).__init__()
		self.arg = arg
	
	def __enter__(self):
		# 获取资源
		print("enter")
		return self

	def __exit__(self,exc_type,ex_val,exc_tb):
		# 释放资源
		print("exit")

	def dosth(self):
		print("doing sth")

with Sample('s') as sample:
	sample.dosth()

import contextlib

@contextlib.contextmanager
def file_open(file_name):
	print("file_open")
	yield {} # 释放资源
	print('file end')

with file_open('hobby.txt') as f:
	print('file processing')