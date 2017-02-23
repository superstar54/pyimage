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
		self.sub = [2, 2]
		self.pos = {}
		self.imagesize = [1000, 1000]

		# bl, bc
		self.mode = 'bc'
		self.modes = ['bl', 'bc', 'br', 'tl', 'tc', 'tr']
		pass
	#
	def calcPosition(self, ):
		# new image size
		maxsize = [0, 0]
		sub = self.sub
		for i in range(sub[0]):
			for image in self.arrange[i]:
				size = self.allimages[image].size
				if size[0] > maxsize[0]: maxsize[0] = size[0]
				if size[1] > maxsize[1]: maxsize[1] = size[1]
		# print(self.arrange)
		self.maxsize = maxsize
		self.imagesize[0] = maxsize[0]*sub[1] + sub[1]*self.interval[1]
		self.imagesize[1] = maxsize[1]*sub[0] + sub[0]*self.interval[0]
		#position of arrange
		print(sub)
		for i in range(sub[0]):
			for j in range(sub[1]):
				size = self.allimages[self.arrange[i][j]].size
				shift = [0, 0]
				#
				shift[1] = int(maxsize[1] - size[1])
				self.pos['bl'][i][j] = [j*maxsize[0] + j*self.interval[1],
							i*maxsize[1] + shift[1] + i*self.interval[0]]
				#
				shift[0] = int((maxsize[0] - size[0])/2.0)
				shift[1] = int(maxsize[1] - size[1])
				self.pos['bc'][i][j] = [j*maxsize[0] + shift[0] + j*self.interval[1],
							i*maxsize[1] + shift[1] + i*self.interval[0]]
				#
				shift[0] = int(maxsize[0] - size[0])
				shift[1] = int(maxsize[1] - size[1])
				self.pos['br'][i][j] = [j*maxsize[0] + shift[0] + j*self.interval[1],
							i*maxsize[1] + shift[1] + i*self.interval[0]]
				#
				self.pos['tl'][i][j] = [j*maxsize[0] + j*self.interval[1],
							i*maxsize[1] + i*self.interval[0]]
				#
				shift[0] = int((maxsize[0] - size[0])/2.0)
				self.pos['tc'][i][j] = [j*maxsize[0] + shift[0] + j*self.interval[1],
							i*maxsize[1] + i*self.interval[0]]
				#
				shift[0] = int(maxsize[0] - size[0])
				self.pos['tr'][i][j] = [j*maxsize[0] + shift[0] + j*self.interval[1],
							i*maxsize[1] + i*self.interval[0]]
		pass

	#
	def mergeImages(self, arrange, interval, mode = 'bc', background = 'w'):
		self.arrange = arrange[:]
		self.sub[0] = len(self.arrange)
		self.sub[1] = len(self.arrange[0])
		self.interval = interval
		self.mode = mode
		for mode in self.modes:
			self.pos[mode] = [[0 for x in range(self.sub[1])] for y in range(self.sub[0])] 
		self.background = background
		# print(self.pos)
		self.calcPosition()
		if self.background.lower() in 'white':
			new_image = Image.new('RGB', self.imagesize, (255, 255, 255))
		elif self.background.lower() in 'black':
			new_image = Image.new('RGB', self.imagesize, (0, 0, 0))
		pos = self.pos[self.mode]
		for i in range(self.sub[0]):
			for j in range(self.sub[1]):
				new_image.paste(self.allimages[arrange[i][j]], (pos[i][j][0], pos[i][j][1]))
		self.outimages['merge.jpg'] = new_image
	#
	def addLabel(self, label, font):
		from PIL import ImageFont
		from PIL import ImageDraw
		img = self.outimages['merge.jpg']
		draw = ImageDraw.Draw(img)
		pos = [0, 0]
		self.labels = ['a', 'a)', '(a)', 
					   'A', 'A)', '(A)',
					   '1', '1)', '(1)']
		if len(label)==1:
			k = ord(label[0])
		elif len(label)==2:
			k = ord(label[0])
		elif len(label)==3:
			k = ord(label[1])
		for i in range(self.sub[0]):
			for j in range(self.sub[1]):
				pos = [j*self.maxsize[0] + j*self.interval[1],
							i*self.maxsize[1] + i*self.interval[0]]
				draw.text(pos,"({0})".format(chr(k)),(0, 0, 0), font = font)
				k += 1
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
			print('cropping {0}'.format(image))
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
			# print(pos)
			im = im.crop(pos)
			# print(im.size)
			self.outimages[image] = im


#--------------------------------
if __name__=='__main__':
	im = Pyimage()
	pass