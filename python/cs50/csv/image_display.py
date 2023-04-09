from PIL import Image
import sys
import os


img=Image.open(sys.argv[1])
img.show()