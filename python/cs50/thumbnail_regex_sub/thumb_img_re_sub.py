import re

myfile = "test.txt"

p1= r"(!\[.*]\(images\/)(.*)(\))"

with open(myfile, "r+") as f:
    data = f.read()
    f.seek(0)
    f.write(re.sub(p1, r"``` {thumbnail} images/\2\n```", data))
    f.truncate()

# this code works really well!!! don't forget to seek()