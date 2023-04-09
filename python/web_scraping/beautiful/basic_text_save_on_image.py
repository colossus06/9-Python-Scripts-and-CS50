from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont




img = Image.open('n.png')
I1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype("/home/elka/Downloads/Copperplate.otf", 65)

# Add Text to an image
I1.text((10, 10), "hello world", align='center', font=myFont, fill =(71, 45, 45))
img.save("zkslfds.png")