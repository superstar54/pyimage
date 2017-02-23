#!/urs/bin/evn python
#crop a minimum box of the non-black or non-white regions in the image. 
from pyimage import Crop
pyim = Crop('.')
images = ['1.jpg']
edge = [50, 50, 50, 50]
# backgound = 'w', 'white' or 'b', 'black'
pyim.cropImages(images, edge, 'w')
pyim.saveImages()