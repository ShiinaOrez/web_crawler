from bs4 import BeautifulSoup
import requests
import login
import url
import run

headers=login.headers

def get_person_name(id):
    # id is illust id
    c=run.reload()
    session=requests.Session()
    session.cookies=c
    url_and_title=url.get_base_url(session,id)
    title=url_and_title['title']
    illuster_name=url.get_illuster_name(title)
    return illuster_name