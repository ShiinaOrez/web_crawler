import requests
import re
import http.cookiejar
import COOKIE
from http import cookies

headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'Referer': '',
}

datas = {
    'pixiv_id': '',
    'password': '',
    'captcha': '',
    'g_reaptcha_response': '',
    'post_key': '',
    'source': 'pc',
    'ref': 'wwwtop_accounts_indes',
    'return_to': 'https://www.pixiv.net/'
}

login_url = 'https://accounts.pixiv.net/login' # login url
post_url = 'https://accounts.pixiv.net/api/login?lang=en' # url to get post_key
daily_url = 'https://www.pixiv.net/ranking.php?mode=daily'

def login(username,password):
    # set account info
    datas['pixiv_id']=username
    datas['password']=password

    s=requests.Session()
    s.headers = headers

    # get login page
    loginPage = s.get(login_url)

    # get post_key
    pattern = re.compile(r'name="post_key" value="(.*?)">')
    postKeys=pattern.findall(loginPage.text)
    datas['post_key'] = postKeys[0]

    # login
    response=s.post(post_url,data=datas)
    if response.status_code != 200:
        print ('please check your pixiv ID and password!')
        return False

    # set cookies
    s.cookies = http.cookiejar.LWPCookieJar(filename='cookies')
    c=open('COOKIE.py','w')
    C=cookies.SimpleCookie()
    print (C)
#   c.writelines('cookies='+str(http.cookiejar.LWPCookieJar(filename='cookies')))
    return s

def reload():
    c=COOKIE.cookies
    s=requests.Session()
    s.cookies=c
    s.headers=headers
    response=s.get(daily_url)
    if response.status_code == 200:
        return {'code': True, 'session':s}
    else:
        return {'code': False, 'session':None}
