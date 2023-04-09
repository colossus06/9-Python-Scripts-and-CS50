#!usr/bin/env

# import libraries
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys

# open image
with open("images2.txt") as n:
    student_lists = n.readlines()
    # print(len(student_lists))
    for a in student_lists:
        #print(f'{a} this is the first')
        img = Image.open("hello.png")

        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype(
            '/home/elka/Downloads/league-spartan-master/LeagueSpartan-Bold.otf', 88)
        # draw.text((x, y),"Sample Text",(r,g,b))
        width, height = img.size
        draw.text((width/2, height/2), a, font=font,
                  anchor="mm", fill="#545454")
        img.save(f'{a}.png')

    # for t in student_lists:
    #     width, height = img.size
    #     a = ImageDraw.Draw(img)
    #     font = ImageFont.truetype('/home/elka/Downloads/league-spartan-master/LeagueSpartan-Bold.otf', 88)
    #     a.text((width/2, height/2), t, font=font, anchor="mm", fill="#545454")
    #     #print(t)
    #     img.save(f'{t}.png')

    # for x in range(0, len(t)):
    #     print(f'./{t}{x}')
    #     print(x)

    # img.save(f'./{student_lists[t]}{x}.png')

    # save image
    # img.save("t.png")
