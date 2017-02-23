#!/urs/bin/evn python
from pyimage import Merge
pyim = Merge(dir = '.')
pyim.scanImages()
arrage = [['1.jpg', '3.jpg'], 
          ['2.jpg', '4.jpg']]
interval = [5, 5]
pyim.mergeImages(arrage, interval)
pyim.saveImages()