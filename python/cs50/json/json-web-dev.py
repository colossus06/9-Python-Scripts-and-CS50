import json
import requests
import subprocess as sp



output = sp.getoutput('whoami --version')
o2= sp.getoutput("curl https://uselessfacts.jsph.pl/random.json")
o3=sp.getoutput("curl https://uselessfacts.jsph.pl/random.json | python -m json.tool")


o4_dict=json.loads(o3)

print (o2)
print(type(o3))
print(type(o4_dict))