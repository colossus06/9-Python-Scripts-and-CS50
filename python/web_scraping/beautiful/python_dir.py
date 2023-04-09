from bs4 import BeautifulSoup
import os
import glob
from pathlib import Path
import requests

# os.chdir(r'/home/elka/Desktop/python-core-projects/beautiful')


exams = glob.glob(
    "/home/elka/Desktop/**/*.html", recursive=True)


#articles= glob.glob("/home/elka/Desktop/python-core-projects/beautiful/**/*.html", recursive=True)


for f in exams:
    with open(f) as r:
        soup = BeautifulSoup(r, "html.parser")
        if soup.title is not None:
            title = soup.title.text.capitalize()
            #f = open("exams.txt",'a')
            #print(title[:-15], file=f, end="\n")
            print(title[:-15])
