# -*- coding:UTF-8 -*-

import requests

url='https://web.wutnews.net/lucky/index/change'

headers={
    'Accept':'application/json',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Cookie':'Hm_lvt_6937a39e5483039406a2ae45f8f1f392=1520176687; PHPSESSID=qhuo8cki85lvm518v50sen9cb3; Hm_lpvt_6937a39e5483039406a2ae45f8f1f392=1520516792',
    'Host':'web.wutnews.net',
    'Referer':'https://web.wutnews.net/act/lucky/boy.html',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}

c=0

while(1):
    r=requests.get(url,headers=headers)
    if '余' in r.json().get('user').get('name'):
        c+=1
        print (r.json().get('info').get('content'))
    if c >= 10 :
        break

