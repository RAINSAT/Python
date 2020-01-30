# 使用python将图片转化为base64字符串
import base64

def img_tobase64(img):
	f = open(img,'rb') #二进制方式打开图文件
	ls_f = base64.b64encode(f.read()) #读取文件内容，转换为base64编码
	f.close()
	print(ls_f)


def base64_img(base64):
	imgdata=base64.b64decode(base64)
	file=open('2.jpg','wb')
	file.write(imgdata)
	file.close()