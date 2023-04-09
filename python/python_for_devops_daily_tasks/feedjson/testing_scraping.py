from bs4 import BeautifulSoup

with open('index.html') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'lxml')
data_titles = []
for a in soup.find('div', class_='list-product with-sidebar').find_all('a'):
    data_titles.append(a['href'].split('/')[1])
print(data_titles)

## Working really well