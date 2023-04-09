import json
from bs4 import BeautifulSoup
import requests
import sys

url=('https://.json')

data = json.loads(requests.get(url)._content)

# for i in data['weather_data']:
#     if str(sys.argv[1]) == i['title']:
#         print("i.ve found", i['title'], i['categories'])

# n= "weather"
# for i in data['weather_data']:
#     if i['title'] == n:
#         print(i['title'], i['href'])
#         print(type(n))

for attrs in data['weather_data']:
    if attrs['title'] == "weather":
        url = attrs['href']
        name = attrs['title']
        print(name, '-', url)
        break
else:
    print('Nothing found!')



# n= "weather"
# for student in data['weather_data']:
#     print(student['title'])

# for student in data['weather_data']:
#     if student['title'] == n:
#         print ("I've found", student['href'])

# example="https://html"

    # title= student['title']
    # url=student['href']
    # category=student['categories']
    # print(category, end="\n\n")



    


