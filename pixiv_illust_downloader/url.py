import requests
import re
import http.cookiejar
from bs4 import BeautifulSoup
import login

headers=login.headers

def get_base_url(s,iid,logger):
    # get page
    response=s.get("https://www.pixiv.net/member_illust.php?mode=medium&illust_id="+str(iid),headers=headers)
    if logger:
        print ('Illust: '+str(iid)+' '+str(response)+'▷')

    if response.status_code == 404:
        return {'msg': '▷-▷-▷>illust is not exist or be deleted!'}
    # use bs4 to resolve HTML text
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
            base_url="https://i.pximg.net/img-original/"+src[a:b]+"_p"
            break
    
    return {'base_url': base_url, 'title': title,}

def get_whole_url(s,base_url,num,tail_url):
    whole_url=base_url+num+tail_url
    headers['Referer']=whole_url
    response=s.get(whole_url,headers=headers)
    return_data={
        'img_url': whole_url,
        'status_code': response.status_code,
    }
    return return_data

def get_illuster_name(s):
    a=s.find('/')
    return s[a+1:]


def get_illust_title(s):
    a=s.find('/')
    return s[:a]

#def test(s,id,base):
#    url='https://www.pixiv.net/ajax/user/'+str(id)+'/profile/all'
#    headers['Referer']=base+str(1)
#    response=s.get(url,headers=headers)
#    print (response.json)


def get_illusts(c,params):
    headers['Referer']='https://www.pixiv.net'
    s=requests.Session()
    s.cookies=c

    response=s.get('https://www.pixiv.net/member.php?id=671593/',headers=headers)
    s=login.resetcookie(s,response.headers['set-cookie'])
#    print(response.text)

#    print(s.cookies)
    response=s.get('https://www.pixiv.net/ajax/user/'+str(params['id'])+'/profile/all',headers=headers) #base_url,params=params,headers=headers)
#    print (response.headers)
#    s=login.resetcookie(s,response.headers['set-cookie'])
    data=response.json()
    if response.status_code != 200:
        return {'list': None,'status_code': response.status_code} 
    else:
        # version---1.2
#        soup=BeautifulSoup(response.text,'html.parser')
#        divs=soup.find_all("div", {"class": "P1uthkK"})
#        for div in divs:
#            sty=str(div['style'])
#            if 'user' not in sty:
#            b=sty.find('_p')
#            sty=sty[:b]
#            a=sty.rindex('/')
#            iid=sty[a+1:]
#            l.append(iid)
#        print (l)
        # version---2.0
        illusts=data.get('body').get('illusts')
#        for illust in illusts:
#            print (illust)
#            iid=illust.get('id')
#            title=illust.get('title')
#            l.append({
#                'id': iid,
#                'title': title,
#            })
#        print (s.cookies)
        return {'list': illusts,'status_code': response.status_code,'cookie':s.cookies}

    