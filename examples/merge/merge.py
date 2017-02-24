#!/urs/bin/evn python
from pyimage import Merge
pyim = Merge(dir = '.')
pyim.scanImages()
intput = '''
bc
line
1.jpg & 2.jpg & 3.jpg \\
line
4.jpg & 5.jpg & 6.jpg \\
line
'''
arrage = [['1.jpg', '3.jpg', '5.jpg'], 
          ['2.jpg', '4.jpg', '6.jpg']]
interval = [15, 15]
pyim.mergeImages(arrage, interval, mode='bc')
pyim.saveImages()