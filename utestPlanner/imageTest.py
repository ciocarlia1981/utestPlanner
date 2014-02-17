__author__ = 'Jonathan'

from PIL import Image, ImageDraw

im = Image.new('RGB', (400, 400), (255, 255, 255))

draw = ImageDraw.Draw(im)

draw.line((100,200, 150,300), fill=128)
draw.rectangle([100,200, 150,300], fill=0x66ff66)

draw.rectangle([120,100, 180,200], fill=0x33ff33)
im.save("test.png")