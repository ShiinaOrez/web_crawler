import requests
import re
from bs4 import BeautifulSoup

url_prefix="https://blog.csdn.net/"
url_rest="/article/list/"

writer_name=input("input the writer_name:")

url=url_prefix+writer_name+url_rest

f=open(writer_name+'_articles.txt','w')

for i in range(1,5):
    blog=requests.get(url+str(i))
    print (blog.status_code)
    blog_text=blog.text
    s=BeautifulSoup(blog_text,'html.parser')
    for arti in s.find_all('li',class_='blog-unit'):
        f.write("""
=========="""+'\n')
        f.writelines('the article url:'+str(arti.a.attrs.get('href'))+'\n')
        title=str(arti.a.h3.text)
        span=arti.a.h3.span
        if span is not None :
            title=title[16:]
        else: title=title[7:] 
        f.writelines('the article title:'+str(title)+'\n')
        for div in arti.div.div.find_all('div'):
            if div.i is not None:
                if 'icon-read' in div.i.attrs.get('class') :
                    f.writelines('visits:'+str(div.span.text)+'\n')
                if 'icon-pinglun' in div.i.attrs.get('class') :
                    f.writelines('comments:'+str(div.span.text)+'\n')
