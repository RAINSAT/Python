# -*- coding: utf-8 -*-
import os
import re

class PICDown(object):
	"""docstring for PICDown"""
	def __init__(self, head=''):
		super(PICDown, self).__init__()
		self.head = head

	def __parser_path(self,pic):
		li = re.split(r'[\\]|[/]', pic)
		name = li[-1]
		li.pop(len(li) - 1)
		path = './'
		if len(li) != 0:
			se = os.path.sep
			path = se.join(li)
			if not os.path.exists(path):
				os.makedirs(path)
		return path, name

	def picture_down_by_url(self,pic_name,pic_url):
		path,name = self.__parser_path(pic_name)
		os.chdir(path)
		from requests import get
		with open(name,'wb') as f:
			if len(self.head)!=0:
				f.write(get(pic_url,self.head).content)
			else:
				f.write(get(pic_url).content)
			f.close()

	def picture_down_by_content(self,pic_name,content):
		path, name = self.__parser_path(pic_name)
		os.chdir(path)
		with open(name,'wb') as f:
			f.write(content)


if __name__ == '__main__':
	pass