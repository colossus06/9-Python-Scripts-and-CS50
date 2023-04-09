from bs4 import BeautifulSoup
import os,glob
import sys


folder_path= "/home/elka/Desktop/python-core-projects/feedjson"

filename=sorted(glob.glob(os.path.join(folder_path, '*.html')))




with open(sys.argv[1]) as f:
    html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'lxml')
    cp=soup.select("section h3")
    cp_cat=soup.find("meta", property="og:title")['content']
  
    for item in cp:

      cp_href=item.a['href'].split('#')[0][2:]
      cp_title=item.span.text
      
    
      ini= '{\n\t"title":'
      end= '\n}'
        
      feed =f'{ini} "{cp_title}",\n\t"url": "{cp_href}",\n\t"category": ["{cp_cat}"]{end},'  
      print(feed)
        
    
            