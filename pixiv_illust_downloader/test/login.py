import requests
import re
import http.cookiejar
#import COOKIE
from http import cookies

headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'Referer': 'https://www.pixiv.net',
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
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

def resetcookie(session,s):
    a=s.find('secure; HttpOnly,')
    s=s[:a]+s[a+18:]
    b=s.find('secure; HttpOnly')
    s=s[:b]+s[b+16:]
    c=s.find('HttpOnly,')
    s=s[:c]+s[c+10:]
    seq=s.split('; ')
    counter=1
    for se in seq:
        if counter == 7:
            break
        a=se.find('=')
        sa=se[:a]
        sb=se[a+1:]
        session.cookies[sa]=sb
    return session

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
    setcookie=response.headers['set-cookie']
    s=resetcookie(s,setcookie)
#    print (s.cookies)

# try to get personal config page and successully!
#    res=s.get('https://www.pixiv.net/setting_user.php',headers=headers,)
#    print (res.text)

    if response.status_code != 200:
        print ('▷-▷-▷>please check your pixiv ID and password!')
        return False

# set cookies
#    s.cookies = http.cookiejar.LWPCookieJar(filename='cookies')
#    c=open('COOKIE.py','w')
#    C=http.cookiejar.CookieJar()
#    print (C)
#   c.writelines('cookies='+str(http.cookiejar.LWPCookieJar(filename='cookies')))
    return s.cookies

def reload():
#    c=COOKIE.cookies
    s=requests.Session()
#    s.cookies=c
    s.headers=headers
    response=s.get(daily_url)
    if response.status_code == 200:
        return {'code': True, 'cookie':s.cookies}
    else:
        return {'code': False, 'cookie':None}
