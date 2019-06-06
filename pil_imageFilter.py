# coding: utf-8

from PIL import Image
from PIL import ImageFilter

img = Image.open("./23.jpg")
# 轮廓滤波
# filt = img.filter(ImageFilter.CONTOUR)
# 边缘增强
# filt = img.filter(ImageFilter.EDGE_ENHANCE)
# 细节增强
# filt = img.filter(ImageFilter.DETAIL)
# 锐化
# filt = img.filter(ImageFilter.SHARPEN)
# 高斯模糊
# filt = img.filter(ImageFilter.GaussianBlur(radius=2))
filt = img.filter(ImageFilter.ModeFilter(size=5))
filt.show()