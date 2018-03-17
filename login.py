# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup

def get_value(s,x):
    for input in s.find_all('input'):
        if input.get('name') == x :
            return input.get('value')

url='https://account.ccnu.edu.cn/cas/login'

r=requests.get(url)
s=BeautifulSoup(r.text,'html.parser',from_encoding='utf-8')
lt=get_value(s,'lt')
exe=get_value(s,'execution')
setc=r.headers.get('set-cookie')
jid=setc[0:49]

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

print ("""


""")
print ('=====account.ccnu.edu.cn=====')
print ('======response.headers=======')

head=r.headers
for i in head:
    print ("||"+i+"||  --->  "+head[i])

print ('=============over===========')
print ('''
''')

print (lt)
print (exe)
