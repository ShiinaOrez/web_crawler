# -*- coding=utf-8 -*-
import urllib.request
import requests
import re
import http.cookiejar
from bs4 import BeautifulSoup

headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'Referer': '',
}

# get提交参数
#params ={
#        'lang': 'en',
#        'source': 'pc',
#        'view_type': 'page',
#        'ref': 'wwwtop_accounts_index'
#        }

# post提交参数
datas = {
        'pixiv_id': 'shiina_orez@qq.com',
        'password': 'mashiro',
        'captcha': '',
        'g_reaptcha_response': '',
        'post_key': '',
        'source': 'pc',
        'ref': 'wwwtop_accounts_indes',
        'return_to': 'https://www.pixiv.net/'
        }

login_url = 'https://accounts.pixiv.net/login' # 登陆的URL
post_url = 'https://accounts.pixiv.net/api/login?lang=en' # 提交POST请求的URL

s = requests.Session()
#ss = urllib.request.Session()
s.headers = headers
#ss.headers = headers

# 获取登录页面
res = s.get(login_url) #, params=params)

# 获取post_key
pattern = re.compile(r'name="post_key" value="(.*?)">')
r = pattern.findall(res.text)
datas['post_key'] = r[0]

# 模拟登录
result = s.post(post_url, data=datas)

# 打印出json信息
#print (result.headers)
#print(result.json())

#ss.cookies = http.cookiejar.LWPCookieJar(filename='cookies')
s.cookies = http.cookiejar.LWPCookieJar(filename='cookies')
Iid=input("Illust ID:")
response=s.get("https://www.pixiv.net/member_illust.php?mode=medium&illust_id="+str(Iid),headers=headers)

opener = urllib.request.build_opener()

print (response)

soup=BeautifulSoup(response.text,'html.parser') # ,from_encoding='utf-8')
row=soup.find_all('img')

for i in row:
    src=str(i.get('src'))
    if "_master" in src:
#        print (src)
        tail_url=list([
            ".jpg",
            ".png",
        ])
        a=src.find("img/")
        b=src.find("_p")
        base_url="https://i.pximg.net/img-original/"+src[a:b]+"_p"
        for i in range(5):
            for tail in tail_url:
                url=base_url+str(i)+tail
                headers['Referer']=url
                res=s.get(url,headers=headers)
#                print (res)
                if res.status_code == 200:
                    print (url)
                    opener.addheaders = [
                        ('User-Agent',headers['User-Agent']),
                        ('Referer',url),
                    ]
                    urllib.request.install_opener(opener)
                    urllib.request.urlretrieve(url,'TEST.png')
