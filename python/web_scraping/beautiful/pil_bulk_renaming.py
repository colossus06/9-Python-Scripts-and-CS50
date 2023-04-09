
from PIL import Image, ImageDraw, ImageFont

width = 512
height = 512
message = "A short introduction to writing incident response playbooks"
font = ImageFont.truetype("/home/elka/Downloads/Copperplate.otf", size=40)

img = Image.new('RGB', (width, height), color='blue')

imgDraw = ImageDraw.Draw(img)
textWidth, textHeight = imgDraw.textsize(message, font=font)
xText = (width - textWidth) / 2
yText = (height - textHeight) / 2

#imgDraw.text((10, 10), message, font=font, fill=(255, 255, 0))
#imgDraw.text((width/2, height/2), message, font=font, fill=(255, 255, 0))
imgDraw.text((xText, yText), message, font=font, fill=(255, 255, 0))


img.save('result.png')