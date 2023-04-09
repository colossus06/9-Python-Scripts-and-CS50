import requests
from bs4 import BeautifulSoup

url = 'https://xml'
r = requests.get(url)
soup = BeautifulSoup(r.content, "xml.parser")

html_elements = soup.find_all("h2", {"class": "story-heading"})

exam_list = []

for exam in html_elements:
    title = exam.text.strip()
    exam_list.append(title)
print(exam_list)