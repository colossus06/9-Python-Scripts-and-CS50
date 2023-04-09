from PIL import Image, ImageDraw, ImageFont
import textwrap
import re


with open("demo_list.txt") as f:
    my_lines = f.readlines()

counter=0

for line2 in my_lines:
    line=line2.rstrip()
    print(line, "here is the")

    img = Image.open("hello.png")

        
    d = ImageDraw.Draw(img)
    art = textwrap.fill(line, 35)


    font = ImageFont.truetype(
        "/home/elka/Downloads/.otf", 60)
        
    #draw = ImageDraw.Draw(img)

    
    position = (img.size[0]/2, img.size[1]/2 +20)
    text_col = (72, 56, 56)
    text_back = (247, 246, 220)

    # left, top, right, bottom = d.textbbox(position, art, font=font)
    # bbox = d.textbbox(position, art, font=font, anchor="mm")

    left, top, right, bottom = d.textbbox(position, art, font=font, anchor="mm")
    d.rounded_rectangle((left-10, top-10, right+10, bottom+10), fill=text_back,  width=3, radius=15)
        
    d.text(position, art, font=font, anchor="mm", fill=text_col)

    img.save(f"dodo{counter}.png")
    counter+=1
    
    # result = len(re.findall(r'\w+', art))
    # match = re.findall(r'\w+', art)

    # print("There are " + str(result) + " words.")
    # print(match)
