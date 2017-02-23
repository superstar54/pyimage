#!/usr/bin/env python
from PIL import Image
import numpy as np
import os

class Pyimage:
	def __init__(self, dir='.'):
		#select input images from current directory
		self.image_extensions = [".jpg", ".png", ".bmp"]
		self.allimages = {}
		self.outimages = {}
		self.dir = dir
		self.scanImages()

		pass

	#
	def scanImages(self):
		print "Scanning " + self.dir
		images = {}
		for i in os.listdir(self.dir):
			b, e = os.path.splitext(i)
			if e.lower() not in self.image_extensions: continue
			im = Image.open(os.path.join(self.dir, i))
			images[i] = im
		self.allimages = images
	#
	def showImages(self,):
		for image in self.allimages:
			print(image)
		pass
	#
	def saveImages(self, dir='results'):
		if not os.path.exists(dir):
			os.makedirs(dir)
		for key, image in self.outimages.items():
			image.save(os.path.join(dir, key))
		pass

#
class Merge(Pyimage):
	'''
	merge and add label
	'''
	def __init__(self, dir):
		Pyimage.__init__(self, dir)
		self.mode = 'bc'
		self.sub = [2, 2]
		self.pos = []
		self.imagesize = [1000, 1000]

		pass
	#
	def calcPosition(self, ):
		# new image size
		maxsize = [0, 0]
		for i in range(self.sub[0]):
			for image in self.arrage[i]:
				size = self.allimages[image].size 
				if size[0] > maxsize[0]: maxsize[0] = size[0]
				if size[1] > maxsize[1]: maxsize[1] = size[1]
		print(self.arrage)
		self.imagesize[0] = maxsize[0]*self.sub[1] + self.sub[1]*self.interval[1]
		self.imagesize[1] = maxsize[1]*self.sub[0] + self.sub[0]*self.interval[0]
		#position of arrange
		# bc
		for i in range(self.sub[0]):
			for j in range(self.sub[1]):
				self.pos[i][j] = [i*maxsize[0] + i*self.interval[0],
							j*maxsize[1] + i*self.interval[1]]
		pass

	#
	def mergeImages(self, arrage, interval):
		self.arrage = arrage[:]
		self.sub[0] = len(self.arrage)
		self.sub[1] = len(self.arrage[0])
		self.pos = arrage[:]  # the same size
		self.interval = interval
		self.calcPosition()
		new_image = Image.new('RGB', self.imagesize)
		for i in range(self.sub[0]):
			for j in range(self.sub[1]):
				print(self.pos[i][j])
				print(self.arrage)
				new_image.paste(self.allimages[arrage[i][j]], (self.pos[i][j][0], self.pos[i][j][1]))
		self.outimages['merge'] = new_image
	#
	def addLabel(self, ):
		pass

#
class Crop(Pyimage):
	'''
	crop a minimum box of the non-black or non-white regions in the image. 
	'''
	def __init__(self, dir):
		Pyimage.__init__(self, dir)

		self.edge = [0, 0, 0, 0]
		pass
	#
	def cropImages(self, images, edge, background = 'w'):
		#
		for image in images:
			im = self.allimages[image]
			size = im.size
			box = [edge[0], edge[1], size[0] - edge[2], size[1] - edge[3]]
			im = im.crop(box)
			im.convert('RGB')
			#
			pixels = np.asarray(im, dtype = 'uint8')
			pos = [100000, 10000000, 0, 0]
			if background=='w' or background=='W':
				for i in range(im.size[1]):
					for j in range(im.size[0]):
						if sum(pixels[i][j]) < 765:
							if j < pos[0]: pos[0] = j
							if i < pos[1]: pos[1] = i
							if j > pos[2]: pos[2] = j
							if i > pos[3]: pos[3] = i
			elif background=='b' or background=='B':
				for i in range(im.size[1]):
					for j in range(im.size[0]):
						if sum(pixels[i][j]) > 0:
							if j < pos[0]: pos[0] = j
							if i < pos[1]: pos[1] = i
							if j > pos[2]: pos[2] = j
							if i > pos[3]: pos[3] = i
			im = im.crop(pos)
			self.outimages[image] = im


#--------------------------------
if __name__=='__main__':
	im = Pyimage()
	pass