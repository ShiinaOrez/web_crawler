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

LOGIN_URL = 'https://accounts.pixiv.net/login'
POST_URL = 'https://accounts.pixiv.net/api/login?lang=en'
DAILY_URL = 'https://www.pixiv.net/ranking.php?mode=daily'

def resetcookie(session,s):
    # session : requests.Session() : None
    # s       : [string]cookie     : SET-COOKIE

    ''' get the available set-cookie '''
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
    # username : string : pixiv account username
    # password : string : pixiv account password

    ''' try to login www.pixiv.net '''
    datas['pixiv_id']=username
    datas['password']=password

    s=requests.Session()
    s.headers = headers

    ''' get login page '''
    loginPage = s.get(LOGIN_URL)

    ''' get the post_key '''
    pattern = re.compile(r'name="post_key" value="(.*?)">')
    postKeys=pattern.findall(loginPage.text)
    datas['post_key'] = postKeys[0]

    ''' make a post request to login '''
    response=s.post(POST_URL,data=datas)
    s=resetcookie(s,response.headers['set-cookie'])

    return_data = {
        "isSignIn": True,
        "cookie": None,
    }
    if response.status_code != 200:
        print ('▷-▷-▷>please check your pixiv ID and password!')
        return_data['isSignIn'] = False
    return_data['cookie'] = s.cookies

    return return_data


def reload():
    ''' get cookie to download a illust '''
    s=requests.Session()
    s.headers=headers
    response=s.get(DAILY_URL)
    if response.status_code == 200:
        return {'code': True, 'cookie':s.cookies}
    else:
        return {'code': False, 'cookie':None}
