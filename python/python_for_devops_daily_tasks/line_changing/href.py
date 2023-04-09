import re
import json
from textwrap import indent
import requests
import sys



url=('https://.json')

data = json.loads(requests.get(url)._content)


my_dict=data['posts']

with open(sys.argv[1], 'r+') as f:   

    content = f.read()
    # student_title=""
    # for ln in content:
    #     if ln.startswith("title: "):
    #         student_title= student_title + ln[8:-2]
    #         print(student_title)
    #     elif ln.startswith("title :"):
    #         student_title=student_title+ln[9:-2]
    #         print(student_title)
    
    k=content.split("##")
    new_content= k[0]
    last_content=new_content.replace('layout: post', 'layout: redirect')
    
    pt= r'title\s?:\s"(.*)"'
    if match := re.search(pt, new_content):
        z=match.group(1)
        print(z)
    # If-statement after search() tests if it succeeded
    if match:
        print('found', z) ## 'found word:cat'
    else:
        print('did not find')

    # extracting href
    def search(title, my_dict):
        return [element['href'] for element in my_dict if element['title'] == title]
    if res := search(z, my_dict):
        print("I've found and it is....")
    else:
        print(" not found")

    # print(res)
    
    def listToString(s):   
    # initialize an empty string
        str1 = " "   
    # return string 
        return (str1.join(s))
    add= listToString(res)
    
    
     

    f.seek(0)
    f.truncate()        
    f.write(re.sub("\n---\n", "\nyou've got this!{}\n---\n".format(add), last_content))

    # Working at last!!!!!!!


    # f.seek(0)
    # f.truncate()        
    # f.write(re.sub("\n---\n", "\nyou've got this!{}\n---\n".format(add), last_content))

    # f.seek(0)
    # f.truncate()
    # f.write(new_content.replace('you've got this!', 'did before'))
    
   
        

    
    # for ln in new_content:
    #     if ln.startswith("title: "):
    #         title= title + ln[6:]
    #         print(title)


# json dict
      
    # my_dict=data['posts']
    # print(type(my_dict))

    # for i in my_dict:
    #     if i['title']== inp:
    #         print("yaay")          

             
    

   
    

    # f.seek(0)
    # f.truncate()        
    # f.write(re.sub(r"\n---\n", "\nredirect_to:\n---\n", new_content))


