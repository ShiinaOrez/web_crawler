import requests
import re
from bs4 import BeautifulSoup

url_prefix="https://blog.csdn.net/"
url_rest="/article/list/"
writer_name=input("input the writer_name:")
url=url_prefix+writer_name+url_rest
f=open(writer_name+'_articles.txt','w')

# get the page 1-5
for i in range(1,5):
    # get the page response
    blog=requests.get(url+str(i))
    # print the status code, 200: OK
    print (blog.status_code)
    # blog_text is the string
    blog_text=blog.text
    s=BeautifulSoup(blog_text,'html.parser')
    # for all of the <div class = "article-item-box csdn-tracking-sttistics">
    for arti in s.find_all('div',class_='article-item-box csdn-tracking-statistics'):
        # delete the <div style = "xxx">
        if arti.attrs.get('style') is not None:
            continue
        # write something
        f.write("""
=========="""+'\n')
        """
        <div>
          <a href = "https://......"> ... </a>
        </div>
        """
        f.writelines('the article url:'+str(arti.a.attrs.get('href'))+'\n')
        title=str(arti.a.text)
        f.writelines('the article title:'+str(title)+'\n')
        """
        <div>
          <div>
            <p> <span> ... </span> 1 </p>
            <p> <span> ... </span> 2 </p>
            ...
          </div>
        </div>
        """
        for div in arti.div.find_all('p'):
            if div.span is not None:
                if 'read-num' in div.span.attrs.get('class') :
                    f.writelines(str(div.span.text)+'\n')
