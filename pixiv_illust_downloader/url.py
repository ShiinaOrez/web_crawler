import requests
import re
import http.cookiejar
from bs4 import BeautifulSoup
import login

headers=login.headers

def get_base_url(s,iid):
    # get page
    response=s.get("https://www.pixiv.net/member_illust.php?mode=medium&illust_id="+str(iid),headers=headers)
    print(response)

    # use bs4 to resolve HTML text
    soup=BeautifulSoup(response.text,'html.parser')
    imgs=soup.find_all('img')

    base_url=''
    for img in imgs:
        src=str(img.get('src'))
        if "_master" in src:
            a=src.find("img/")
            b=src.find("_p")
            base_url="https://i.pximg.net/img-original/"+src[a:b]+"_p"
    
    return base_url

def get_whole_url(s,base_url,num,tail_url):
    whole_url=base_url+num+tail_url
    headers['Referer']=whole_url
    response=s.get(whole_url,headers=headers)
    return_data={
        'img_url': whole_url,
        'status_code': response.status_code,
    }
    return return_data