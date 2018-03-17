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
    re.sub(pat,"",title)
    print ('the article title:',title)

ss="		   ss		"
re.sub(pat,"",ss)
print (ss)
