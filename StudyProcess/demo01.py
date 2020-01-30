#coding:utf-8
from collections.abc import Sized # 抽象基类
# 抽象基类
class Company(object):
 	"""docstring for Company"""
 	def __init__(self, arg):
 		super(Company, self).__init__()
 		self.arg = arg
 	
 	def __len__(self):
 		return len(self.arg)
com = Company(['a','b'])
# print(hasattr(com,'__len__'))
# 我们需要强制某个子类必须实现某些方法
# 需要设计一个抽象基类，指定子类必须实现某些方法

# 使用 instance 而不是 type
print(isinstance(com,Sized))

# 如何去模拟一个抽象基类
# 1.让基类方法抛一个异常
class CacheBase(object):
	def get(self,key):
		raise NotImplementedError

	def set(self,key,value):
		raise NotImplementedError

# 2. abc模块
import abc
class CacheBaser(metaclass=abc.ABCMeta):
	
	@abc.abstractmethod
	def get(self,key):
		pass

	@abc.abstractmethod
	def set(self,key,value):
		pass
		