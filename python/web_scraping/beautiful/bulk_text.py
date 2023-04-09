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
    #exam = "Hello exams"
    art = textwrap.fill(line, 35)


    #image = Image.new("RGB", (500, 100), "white")
    font = ImageFont.truetype(
        "/home/elka/Downloads/league-spartan-master/LeagueSpartan-Bold.otf", 60)
    #draw = ImageDraw.Draw(img)
    position = (150, img.size[1]/2-50, 60, -150)


    left, top, right, bottom = d.textbbox(position, art, font=font)
    bbox = d.textbbox(position, art, font=font)
    text_back = (247, 246, 220)
    d.rounded_rectangle((left-20, top-20, right+20, bottom+20),
                        fill=text_back, width=3, radius=15)

    text_col = (72, 56, 56)
    d.text(position, art, font=font, fill=text_col)

    img.save(f"dodo{counter}.png")
    counter+=1


#f.seek(0,0)
f.close()


    # result = len(re.findall(r'\w+', art))
    # match = re.findall(r'\w+', art)

    # print("There are " + str(result) + " words.")
    # print(match)
