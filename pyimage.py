#!/usr/bin/env python
from PIL import Image
import numpy as np
import os

class Pyimage():
	def __init__(self, ):
		#select input images from current directory
		self.image_extensions = [".jpg", ".png", ".bmp"]
		self.images = []
		self.dir = '.'
		pass

	def getImages(self, dir):
		self.dir = dir
		print "Scanning " + dir
		images = {}
		for i in os.listdir(dir):
			b, e = os.path.splitext(i)
			if e.lower() not in self.image_extensions: continue
			im = Image.open(os.path.join(self.dir, i))
			images[i] = im
		self.images = images
		# print(self.images)
	#
	def cropImages(self, edge):
		for image in self.images:
			im = self.images[image]
			pixels = np.asarray(im, dtype = 'uint8')
			pos = [100000, 10000000, 0, 0]			
			for i in range(edge[0], im.size[1] - edge[2]):
				for j in range(edge[1], im.size[0] - edge[3]):
					if sum(pixels[i][j]) > 0:
						if j < pos[0]: pos[0] = j
						if i < pos[1]: pos[1] = i
						if j > pos[2]: pos[2] = j
						if i > pos[3]: pos[3] = i
			im = im.crop(pos)
			self.images[image] = im
		pass

	#
	def mergeImages(self, arrage, interval):
		# calculate size
		maxsize = [0, 0]
		for i in range(len(arrage)):
			for image in arrage[i]:
				tmpsize = self.images[image].size 
				if tmpsize[0] > maxsize[0]: maxsize[0] = tmpsize[0]
				if tmpsize[1] > maxsize[1]: maxsize[1] = tmpsize[1]
		size = [0, 0]
		size[0] = len(arrage)
		size[1] = len(arrage[0])
		new_image = Image.new('RGB', (maxsize[0]*size[1], maxsize[1]*size[0]))
		print(size, maxsize)
		pos = [0, 0]
		for i in range(size[0]):
			for j in range(size[1]):
				pos[0] = j*maxsize[0]
				pos[1] = i*maxsize[1]
				new_image.paste(self.images[arrage[i][j]], (pos[0], pos[1]))
		self.new_image = new_image
		self.output = 'output.png'
		self.new_image.save(self.output)
		pass
	#
	def showImages(self,):
		for image in self.images:
			print(image)
		pass

#--------------------------------
pyim = Pyimage()
pyim.getImages('/home/xing/xcp2k/surfaces/ceo2/111/relax/pto2')
# pyim.showImages()

jobs = {'t_e1_o':None ,
        't_e1_o_pt': None ,
        't_e1_ce': None ,
        't_e1_ce_pt': None ,
        's_e3_ce': None ,
        's_e3_ce_pt': None ,}
prefix = 'ceo2-111-pto2-'
suffix = ['-top.png', '-side.png']
arrage = [[ x for x in range(6)], [ x for x in range(6)]]
# print(arrage)
jobs.keys()[5]
for i in range(2):
	for j in range(6):
		arrage[i][j] = prefix + jobs.keys()[j] + suffix[i]
print(arrage)
edge = [0, 0, 100, 0]
pyim.cropImages(edge)
interval = [0, 0]
pyim.mergeImages(arrage, interval)
# catIm = Image.open('/home/xing/xcp2k/surfaces/ceo2/111/relax/pto2/ceo2-111-pto2-s_e3_ce-top.png')
# print(catIm.size)
# catIm.show()