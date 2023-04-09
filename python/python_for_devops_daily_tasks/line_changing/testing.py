import json
import re

file = """{
  "weather_data": [
 
  ]
}
"""
inp3=input("s")

title2= ""

data=json.loads(file)
my_dict=data['weather_data']
print(type(my_dict))

for i in my_dict:
    if i['title']== inp3:
        print("yaay")

colour_dict = [
    {'main_colour': 'red', 'count': 1},
    {'main_colour': 'blue', 'count': 5},
    {'main_colour': 'green', 'count': 10},
]

# colours = ["blue", "blue", "red", "greed", "red", "black"]


# for colour in colours:
#     for dic in colour_dict:
#         if dic['main_colour'] == colour:
#             print("yaaay")

# colour=input("")

# for i in colour_dict:
#     if i['main_colour'] == colour:
#         print("sdfsfs")