#!/usr/bin/python
#-*- coding: UTF-8 -*- 

import os
import sys
from PIL import Image

# 父目录
p_path = os.path.dirname(os.getcwd()) + '/' 

size_list = [20, 29, 40, 60]
scale_list = [2, 3] # @2x, @3x

def main(file_name):
	# 图片路径
	pic_path = p_path + file_name
	if not os.path.exists(pic_path):
		print '图片不存在'
		return

	# 生成的图片的存放文件夹
	name = os.path.splitext(file_name)[0] + '_images'

	# 存放路径
	deal_path = p_path + name + '/'

	# 判断是否存在该路径，不存在就创建
	if not os.path.exists(deal_path):
		os.makedirs(deal_path)

	#读取图片
	im = Image.open(pic_path)

	#生成相应大小的图片
	for size in size_list:
		for scale in scale_list:
			w = h = size * scale
			# print 'w = ' + str(w) + ' : ' + 'h = ' + str(h)
			f_name = str(size) + 'x' + str(size) + '@' + str(scale) + 'x.png'
			# print f_name
			out = im.resize((w, h), Image.ANTIALIAS)
			# print deal_path + f_name
			out.save(deal_path + f_name)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:	
		print '请输入图片名称'
	
