import requests
import login
import url
import profile
import run

cookie=run.signin()
session=requests.Session()
headers=login.headers
session.cookies=cookie

url='https://www.pixiv.net/member_illust.php?mode=medium&illust_id=69178311'

r=session.get(url,headers=headers)

print(r)
print(r.text)