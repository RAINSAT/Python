# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 20:36:06 2019

@author: zyxwy
"""

from PIL import Image,ImageFilter
import numpy as np

class Lut(object):
    def __init__(self,path,param):
        self.path = path
        self.params = param
    
    def feeting(self):
        src = Image.open(self.path)
        src.show()
        Img = np.asarray(Image.open(self.path).convert('RGB'))
        Img1 = np.sqrt(Img*[1.0,0.0,0.0])*self.params
        Img2 = Img*[0.0,1.0,1.0]
        Img = Img1 + Img2
        Img = Image.fromarray(np.array(Img).astype('uint8'))
        Img.show()
    
    # ImageFilter.EMBOSS 浮雕效果滤镜
    # ImageFilter.EDGE_ENHANCE 凸显边界
    # ImageFilter.EDGE_ENHANCE_MORE 加倍凸显边界
    # ImageFilter.FIND_EDGES 只保留边界
    # ImageFilter.CONTOUR 铅笔画效果
    # ImageFilter.SMOOTH_MORE 平滑滤镜
    # ImageFilter.BLUR 模糊滤镜
    def lut_PIL(self):
        src = Image.open(self.path)
        im2 = src.filter(ImageFilter.EMBOSS) #模糊滤镜
        im2.save('./img/qm_1.jpg')
        
        
        
        
if __name__ == '__main__':
    lut = Lut('./img/55.jpg',0.9)
    lut.lut_PIL()
        