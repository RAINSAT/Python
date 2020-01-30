#!/usr/bin/env 


class A(object):

	# 类变量
	a = 1
	"""docstring for A"""
	def __init__(self, x):
		super(A, self).__init__()
		self.x = x
s = A(3)
A.a = 11
s.a = 100 # 这里相当于 self.a = 100
print(s.x,s.a) # 如果在实例变量中找不到，会向上查找
print(A.a) # A 不会向下查找


# 数据封装和私有属性
class User(object):
	"""docstring for User"""
	def __init__(self, name):
		super(User, self).__init__()
		# 私有属性
		self.__name = name

	def get_name(self):
		return self.__name

user = User('tim')
print(user.get_name())
print(user._User__name)# obj._classname__property


# 对象的自省机制
# 通过一定的机制查询到对象的内部结构
class Person(object):
	"""
	人
	"""
	sname = 'user'
	def __init__(self, arg):
		super(Person, self).__init__()
		self.arg = arg

class Student(Person):
	def __init__(self,school_name):
		self.school_name = school_name

stu = Student('hello')
print(stu.__dict__)
print(stu.sname)
print(Person.__dict__)
stu.__dict__['school_addr'] = 'Beijing'
print(stu.__dict__)
print(dir(stu))


# super
class B(object):
	"""B"""
	def __init__(self, arg):
		super(B, self).__init__() # python2
		self.arg = arg
		print('B')

class C(B):
	"""C"""
	def __init__(self, arg):
		super().__init__(arg) #python3
		self.arg = arg
		print("C")

class D(B):
	"""D"""
	def __init__(self, age):
		super(D, self).__init__(age)
		self.age = age
		print("D")

class E(C,D):
	"""E"""
	def __init__(self, name):
		super(E, self).__init__(name)
		self.name = name
		print('E')

e = E('a')
print(E.__mro__)


# mixin