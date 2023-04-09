import textwrap

strs = "In my project, I have a bunch of strings that are read in from a file. Most of them, when printed in the command console, exceed 80 characters in length and wrap around, looking ugly."
print(textwrap.fill(strs, 30))
