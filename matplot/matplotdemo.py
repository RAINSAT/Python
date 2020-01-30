# -*-coding:utf8 -*-
"""
Backend: 处理把图显示到哪里和画到哪里

Artist:图像显示成什么样子

Script:pyplot Pyhthon 语法 和 API

"""

import matplotlib.pyplot as plt
import numpy as np

"""

# 散点图

# x = numpy.random.normal(0, 1, 1024)
# # y = numpy.sin(x)
# y = numpy.random.normal(0, 1, 1024)
# ply.scatter(x, y, s=numpy.random.rand(1024)*50, c=numpy.random.rand(1024), alpha=0.7)
# ply.show()

# 'm^:' 虚线红色：'r--
"""

class matplot(object):
	"""docstring for matplot"""
	def __init__(self):
		super(matplot, self).__init__()
	
	def drawLineByRandom(self,start,end,pointnum):
		x = np.linspace(start,end,pointnum)
		y = 2 * x + 4
		plt.plot(x,y,'*')
		plt.xlabel("this is x")
		plt.ylabel('this is y')
		plt.title('title')
		plt.show()
        

if __name__ == '__main__':
	mat = matplot()
	mat.drawLineByRandom(1,25,50)
