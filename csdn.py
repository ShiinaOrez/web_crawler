import requests
import re
from bs4 import BeautifulSoup

url_prefix="https://blog.csdn.net/"

writer_name=input("input the writer_name:")

url=url_prefix+writer_name

blog=requests.get(url)

print (blog.status_code)

blog_text=blog.text

s=BeautifulSoup(blog_text,'html.parser')

pat=re.compile('\s')

for arti in s.find_all('li',class_='blog-unit'):
    print ("""
==========""")
    print ('the article url:',arti.a.attrs.get('href'))
    title=str(arti.a.h3.text)
    span=arti.a.h3.span
    if span is not None :
        title=title[16:]
    else: title=title[7:] 
    print ('the article title:',title)
    div=arti.div.div
    for d in div :
        if d.span is not None :
            if "read" in d.i.class_:
                print ('visits:',d.span.text)
            if "pinglun" in d.i.class_:
                print ('comments:',d.span.text)

