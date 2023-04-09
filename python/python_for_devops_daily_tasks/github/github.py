import requests
import json
import pdb



response=requests.get("https://api.github.com/users/colossus06")
print(type(response.json))
ap=response.json()
# print(ap)
# for first, last in ap:
    # print("first is: ", first, "last one is: ", last)
# print(f"Bio is: {ap['bio']} followers are: {ap['followers']}")

pdb.set_trace()
print("-----------------------")
print(json.dumps(ap, indent = 2))
print(json.dumps(ap, indent = "\t"))


