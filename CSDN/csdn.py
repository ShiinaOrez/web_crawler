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
#    print (blog_text)
    for arti in s.find_all('div',class_='article-item-box csdn-tracking-statistics'):
        if arti.attrs.get('style') is not None:
            continue
        f.write("""
=========="""+'\n')
        f.writelines('the article url:'+str(arti.a.attrs.get('href'))+'\n')
        title=str(arti.a.text)
        """span=arti.a.h3.span
        if span is not None :
            title=title[16:]
        else: title=title[7:] """
        f.writelines('the article title:'+str(title)+'\n')
        for div in arti.div.find_all('p'):
            if div.span is not None:
                if 'read-num' in div.span.attrs.get('class') :
                    f.writelines(str(div.span.text)+'\n')
