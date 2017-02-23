#!/urs/bin/evn python
from pyimage import Crop
from pyimage import Merge
from PIL import ImageFont
from PIL import ImageDraw

#crop a minimum box of the non-black or non-white regions in the image. 
crop = Crop('.')
images = ['s_o_1.png', 's_pt_1.png', 't_o_1.png', 'to_o_1.png', 'to_pt_1.png', 't_pt_1.png', 's_o_2.png', 's_pt_2.png', 't_o_2.png', 'to_o_2.png', 'to_pt_2.png', 't_pt_2.png']
edge = [30, 30, 30, 30]
# backgound = 'w', 'white' or 'b', 'black'
# crop.cropImages(images, edge, 'b')
# crop.saveImages('crops')

#
merge = Merge(dir = 'crops')
merge.scanImages()
arrage = [['s_o_1.png', 's_pt_1.png', 't_o_1.png', 'to_o_1.png', 'to_pt_1.png', 't_pt_1.png'], 
          ['s_o_2.png', 's_pt_2.png', 't_o_2.png', 'to_o_2.png', 'to_pt_2.png', 't_pt_2.png']]
interval = [200, 100]
# mode, bc: bottom, center; 
merge.mergeImages(arrage, interval, mode='bc', background = 'w')
font = ImageFont.truetype(
		"/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf",80)
merge.addLabel('a', font)
merge.saveImages()

# [112, 115, 813, 696], 701, 581