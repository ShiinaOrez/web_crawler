from bs4 import BeautifulSoup
import requests
import login
import url
import run

headers=login.headers

def get_person_name(session,id):
    # session : requests.Session() : None
    # id      : integer            : illustor ID

    ''' get illustor name '''
    PROFILE_URL = "https://www.pixiv.net/member.php?id="

    response=session.get(PROFILE_URL+str(id),headers=headers)
    txt=response.text
    a=txt.find('preload:')
    b=txt.find('<!-- Google Tag Manager -->')
    preload=txt[a:b]
    a=preload.find('region')
    preload=preload[:a]
    partten='name'
    a=preload.find(partten)
    b=a+7
    while preload[b] is not '"':
        b+=1
    illustname=preload[a+7:b]

    return illustname
