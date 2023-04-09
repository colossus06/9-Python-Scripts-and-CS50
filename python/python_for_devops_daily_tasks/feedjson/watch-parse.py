
import re
import sys


import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern= r'src="(https?:\/\/)?(www)?.youtube\.com\/embed\/(\w+)\"'
    

    if match:= re.search(pattern, s):
        k = ("https://youtu.be/")
        t = match.group(3)
        return k+t
  
if __name__ == "__main__":
    main() 

