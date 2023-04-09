import re
import sys


def main():
    pattern = r'title:[\s]"(.*?)(")'
   
    with open(sys.argv[1], "r+") as file:
        text = file.read()
        match= re.search(pattern, text)
        x= match.group(1)
        text = re.sub(pattern,r'pattern', text)
        text=text.split("#", 1)   
        # re.search('(.*?---.*?)---', text).group(1)
        text[0]= f":orphan:\n {x}"
        n= text[0] + text[1]
        file.seek(0, 0) # seek to beginning
        file.write(n)
        file.truncate()
         # get rid of any trailing characters

if __name__ == "__main__":
    main() 