import PIL
from PIL import Image
from tkinter.filedialog import *


file_path=askopenfile()
img=PIL.Image.open(file_path)

h, w=img.size

img = img.resize((h,w), PIL.Image.Antialias)

save_path= asksaveasfile()
img.save(save_path)