import requests
import re
import http.cookiejar
from bs4 import BeautifulSoup
import login

headers=login.headers

def get_base_url(s, iid, logger):
    # s      : requests.Session() : None
    # iid    : integer            : illust ID
    # logger : bool               : Print Log?

    ''' try to get illust page '''
    BASE_URL = "https://www.pixiv.net/member_illust.php?mode=medium&illust_id="

    response=s.get(BASE_URL+str(iid),headers=headers)
    if logger:
        print ('Illust: '+str(iid)+' '+str(response)+'▷')
    if response.status_code == 404:
        return {'msg': '▷-▷-▷>illust is not exist or be deleted!'}

    ''' try to find <img> in HTML.text '''
    soup=BeautifulSoup(response.text,'html.parser')
    imgs=soup.find_all('img')

    base_url=''
    title=''

    for img in imgs:
        src=str(img.get('src'))
        if "_master" in src:
            title=str(img.get('title'))
            a=src.find("img/")
            b=src.find("_p")
            # src[a:b] is the /20xx/xx/xx/xx/xxxx/
            base_url="https://i.pximg.net/img-original/"+src[a:b]+"_p"
            break

    return_data = {
        "base_url": base_url,
        "title": title,
    }
    return return_data


def get_whole_url(s, base_url, num, tail_url):
    # s        : requests.Session() : None
    # base_url : string             : None
    # num      : string             : p_"num"
    # tail_url : string             : ".jpg" or ".png"

    ''' try the pictrue really exist '''
    whole_url=base_url+num+tail_url
    headers['Referer']=whole_url
    response=s.get(whole_url,headers=headers)

    return_data={
        'img_url': whole_url,
        'status_code': response.status_code,
    }
    return return_data

def get_illuster_name(s):
    # s : string : origin string

    ''' just return a new slice of string '''
    a=s.find('/')
    return s[a+1:]


def get_illust_title(s):
    # s : string : origin string

    ''' just return a new slice of string '''
    a=s.find('/')
    return s[:a]


def get_illusts(c,params):
    # c      : [string]cookie : Session().cookies
    # params : dictionary     : parameters

    ''' get the illusts by json! '''
    BASE_PROFILE = "https://www.pixiv.net/member.php?id=/"
    BASE_JSON = "https://www.pixiv.net/ajax/user/"
    TAIL_JSON = "/profile/all"

    ''' reload session cookie'''
    s=requests.Session()
    s.cookies=c

    ''' test the json URL is avaliable? '''
    response=s.get(BASE_PROFILE+str(params['id']),headers=headers)
    s=login.resetcookie(s,response.headers['set-cookie'])

    ''' get json '''
    response=s.get(BASE_JSON+str(params['id'])+TAIL_JSON,headers=headers)
    data=response.json()

    return_data = {
        "status_code": response.status_code,
    }
    if response.status_code != 200:
        return_data['list'] = None
    else:
        return_data['list'] = data.get('body').get('illusts')
        return_data['cookie'] = s.cookies

    return return_data

