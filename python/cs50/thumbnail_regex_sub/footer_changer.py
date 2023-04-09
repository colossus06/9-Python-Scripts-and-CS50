import re
import glob
import os


path = os.getcwd()
print("Current working directory: {0}".format(path))
print("os.getcwd() returns an object of type: {0}".format(type(path)))

os.chdir('/home/elka/Desktop/python-core-projects/thumbnail_regex_sub')
print(os.getcwd())




for filepath in glob.iglob('./**/*.md', recursive=True):
    p1= r'>\s\**(.*\))(.(.*)\**|.\s(.*)\**|.\**|.\**)'


    with open(filepath, "r+") as f:
        data = f.read()
        f.seek(0)
        f.write(re.sub(p1, r":::{seealso}\n\1 \2\n:::", data))
        f.truncate()