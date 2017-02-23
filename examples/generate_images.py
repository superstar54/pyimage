#!/urs/bin/evn python
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os


font1 = ImageFont.truetype(
		"/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf",50)
font2 = ImageFont.truetype(
	"/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf",10)
#merge
for i in range(1, 5):
	img = Image.new('RGB', [100, 100], (255, 255, 255))
	draw = ImageDraw.Draw(img)
	draw.text((25, 25),"{0}".format(i),(120,20,20), font = font1)
	img.save('{0}.jpg'.format(i))
	os.system('mv {0}.jpg merges'.format(i))


#crop
img = Image.new('RGB', [500, 500], (255, 255, 255))
draw = ImageDraw.Draw(img)
draw.text((50, 200),"Hello world!",(120,20,20), font = font1)
draw.text((440, 480),"Pyimage",(120,20,20), font = font2)
img.save('crops/1.jpg')


