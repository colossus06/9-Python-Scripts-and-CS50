import re
import glob
import os


os.chdir('')

for filepath in glob.iglob('./**/*.md', recursive=True):
    p1= r"(!\[.*]\(images\/)(.*)(\))"

    with open(filepath, "r+") as f:
        data = f.read()
        f.seek(0)
        match=re.finditer(p1, data)
        f.write(re.sub(p1, r"``` {thumbnail} images/\2\n```", data))
        f.truncate()

        if r'="images/' in data and not match:
            print("there may only be html in ")
            
        elif r'="images/' in data and match:
            print("There are html and markdown imges")
            for i in match:
                print(f"Renamed these files: {i.group(2)}")
        elif r'="images/' not in data and match:
            print("no html but there are markdown images")
            for i in match:
                print(f"Renamed these files: {i.group(2)}")
           