import re
import sys


pattern = r'title:[\s]"(.*?)(")'
pattern2 = r'^---([\s\S]*)(\---)'  # match --- and --- all the things between

with open(sys.argv[1], "r+") as file:
    text = file.read()
    match = re.sub(pattern2, " ", text)

    match2 = re.search(pattern, text)
    k2= match2.group(1)
    

    chars = " #'"
    chars2 = ":?!,$&"

    for i in chars:
        k2= k2.replace(i, "-").lower()
    for i in chars2:
        k2=k2.replace(i,"").lower()
    
    k = f":orphan:\n({k2})=\n# {match2.group(1)}\n{match}"

    # print(k)
    # print(k2)
    # n = k+match
    # print(k)
    # print(n)
    # print(k)

    file.seek(0, 0) #seek to beginning
    file.write(k)
    file.truncate()
