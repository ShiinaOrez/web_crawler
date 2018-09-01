import requests
import login
from http import cookies

url='https://www.pixiv.net/member.php?id=3016'
id='3016'
headers=login.headers

username=input('username:')
password=input('password:')
cookie=login.login(username,password)

session=requests.Session()
session.cookies=cookie

response=session.get(url,headers=headers)

txt=response.text
a=txt.find('preload:')
b=txt.find('<!-- Google Tag Manager -->')

preload=txt[a:b]
partten='''"userId":"''' + str(id) + '''","name":"'''
a=preload.find(partten)
b=a+len(partten)+1
while preload[b] is not '"':
    b+=1
illustname=preload[a+len(partten):b]
print (illustname)

