from PIL import Image, ImageOps
import sys
import os
import os.path
from os import path


images = []


if len(sys.argv) > 3:
    sys.exit("Ooops... too many command lines")
elif len(sys.argv) <3:
    sys.exit("Too few arguments")
elif len(sys.argv) ==3:
    f, ext=os.path.splitext(sys.argv[1])
    k, ext2 = os.path.splitext(sys.argv[2])

    exts= [".jpg", ".jpeg", ".png"]
    
    if ext not in exts:
        sys.exit("Invalid unfortunately")
    if ext2 not in exts:
        sys.exit("Wow...Invalid unfortunately")

    elif ext != ext2:
        sys.exit("please use identical extensions")
    
    elif not path.exists(sys.argv[1]):
        sys.exit("Give me e valid name")



img=Image.open(sys.argv[1])
img2=Image.open(sys.argv[2])

img = ImageOps.fit(img, (100, 100), method = 0,
                   bleed = 0.0, centering =(0.5, 0.5))

img.paste(img2)
img=img.save("test.png", format="png")

