#!/usr/bin/env python
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

# edge: top, bottom, left, right
edge = [10, 10, 5, 5]
pyim.mergeImages(arrage, interval, edge, mode='bc')
pyim.addLabels('1)', fontsize=20, fill='white')
pyim.saveImages()