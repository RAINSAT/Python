# -*- coding:utf-8 -*-

from PIL import Image
from PIL import ImageDraw
from PIL import  ImageFont

im = Image.open(r'E:\Users\Pictures\Camera Roll\2.jpg', 'r')

# im.show()

# print(im)

draw = ImageDraw.Draw(im)

# my_font = ImageFont.truetype(font=ImageFont.load_default(), size=14)

#my_font = ImageFont.load_path('Consolas.ttf')
#draw.text((100, 200), "hello", font=my_font)

im.show()
