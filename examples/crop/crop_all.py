#!/usr/bin/env python
#crop a minimum box of the non-black or non-white regions in the image. 
from pyimage import Crop
pyim = Crop('.')
images = pyim.allimages
edge = [50, 50, 50, 50]
# backgound = 'w', 'white' or 'b', 'black'
pyim.cropImages(images, edge, 'w')
pyim.saveImages()