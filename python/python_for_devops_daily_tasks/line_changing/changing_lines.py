import re
import json
from textwrap import indent
import requests
import sys



url=('https://.json')

data = json.loads(requests.get(url)._content)


my_dict=data['posts']

# # print(test_list)
# def search(title, my_dict):
#     return [element['href'] for element in my_dict if element['title'] == title] 
# res = search(inp, my_dict)

# # Python program to convert a list
# # to string using join() function
   
# def listToString(s):
   
#     # initialize an empty string
#     str1 = " "
   
#     # return string 
#     return (str1.join(s))      
       
# # Driver code  
# print(listToString(res))
# inp=input()

# Replace variables in file
with open('test.md', 'r+') as f:
    student_title=""
    for ln in f:
        if ln.startswith("title: "):
            student_title= student_title + ln[8:-2]
            print(student_title)
        elif ln.startswith("title :"):
            student_title=student_title+ln[9:-2]
            print(student_title)

    content = f.read()
    content.replace('your note: ', 'with this')
    k=content.split("##")
    new_content= k[0]
    
    

    # extracting href
    def search(title, my_dict):
        return [element['href'] for element in my_dict if element['title'] == title]
    if res := search(student_title, my_dict):
        print("I've found")
    else:
        print(" not found")

    # print(res)
    
    def listToString(s):   
    # initialize an empty string
        str1 = " "   
    # return string 
        return (str1.join(s))
    
    print(listToString(res))
   

    # Python program to convert a list
    # to string using join() function
    
    # def listToString(s):
    
    #     # initialize an empty string
    #     str1 = " "
    
    #     # return string 
    #     return (str1.join(s))      
        
    # # Driver code  
    # print(listToString(res))





    

 
    # f.seek(0)
    # f.truncate()
    # f.write(new_content.replace('saying: tell me', 'saying: no'))
    # f.seek(0)
    # f.truncate()        
    # f.write(re.sub(r"\n---\n", "\ntell me more/\n---\n", new_content))
   
        

    
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


