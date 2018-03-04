# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup

url='https://account.ccnu.edu.cn/cas/login'

r=requests.get(url)

html_doc=r.text
s=BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
for input in s.find_all('input'):
    if input.get('name') == 'lt':
        lt=input.get('value')
    if input.get('name') == 'execution':
        exe=input.get('value')

setc=r.headers.get('set-cookie')

jid=setc[0:49]

print (setc)

payload={
    "username":'2017211712',
    "password":'sry19990512',
    "lt":lt,
    "execution":exe,
    "_eventId":'submit',
    "submit":'登录'
}

headers={
    "Accept":'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    "Accept-Encoding":'gzip, deflate, br',
    "Accept-Language":'zh-CN,zh;q=0.9',
    "Cache-Control":'max-age=0',
    "Connection":'keep-alive',
    "Content-Length":159,
    "Content-Type":'application/x-www-form-urlencoded',
    "Cookie":jid,
    "Host":'account.ccnu.edu.cn',
    "Origin":'https://account.ccnu.edu.cn',
    "Referer":'https://account.ccnu.edu.cn/cas/login',
    "Upgrade-Insecure-Requests":1,
    "User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

r=requests.post(url,data=payload,headers=headers)

print (r.headers,r.status_code)
