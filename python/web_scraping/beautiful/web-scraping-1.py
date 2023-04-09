
from turtle import title
import requests
from bs4 import BeautifulSoup



# with open("becoming-a-malware-analyst.html") as htmlf:
#     soup= BeautifulSoup(htmlf, 'lxml')


# article= soup.find("div",class_="article").text
# print(article)
# match= soup.title.text[:-15]
# print(match)
#print(match.prettify())


import requests
from bs4 import BeautifulSoup
url = 'https://'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.title, 'lxml')
print("List of all the h1, h2, h3 :")
for heading in soup.find_all():
    print(heading.name + ' ' + heading.text.strip())