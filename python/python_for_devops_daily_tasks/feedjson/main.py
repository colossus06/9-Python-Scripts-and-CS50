from bs4 import BeautifulSoup
import os,glob



for filename in sorted(glob.glob("/home/elka/Desktop/*.html", recursive = True)):
    


    with open(filename) as f:
        html_content = f.read()
       
        soup = BeautifulSoup(html_content, 'lxml')             
        s=soup.select("li p a")
        c=soup.find("meta", property="og:title")

        for a in s:
            href= a['href'][2:].split("#")[0]
            an= a.text
            cat= c["content"]
            ini= '{\n\t"title":'
            end= '\n}'
        
            feed =f'{ini} "{an}",\n\t"url": "{href}",\n\t"category": ["{cat}"]{end},'            
            

            # t.write(feed)
            print(feed)
        

                

