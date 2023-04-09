
import requests

from bs4 import BeautifulSoup

url = "https://www.errbufferoverfl.me/sitemap.xml"


r= requests.get(url)

sp= BeautifulSoup(r.text, 'lmxl')

links= sp.find_all('loc')

print(len(links))