import login,url,download
import os
import sys
import time
import requests
import profile

Username=''
Password=''

def reload():
    re=login.reload()
    cookie=re['cookie']
    return cookie

def signin():
    Username=input("Your pixiv account: ")
    Password=input("Your pixiv password: ")

    cookie=login.login(Username,Password)
    print('    ===================')
    print('===>login successfully!')
    return cookie

def run_by_iid(session,Iid):

    url_and_title=url.get_base_url(session, Iid, True)
    try:
        print (url_and_title['msg'])
        return
    except:
        base_url=url_and_title['base_url']
        title=url_and_title['title']
        illuster_name=url.get_illuster_name(title)
        illust_title=url.get_illust_title(title)

    counter=0
    jpgFlag=True
    pngFlag=True
    while jpgFlag or pngFlag:
        time.sleep(1)
        _data=url.get_whole_url(session,base_url,str(counter),'.jpg')
        if _data['status_code'] != 200:
            jpgFlag=False
        else:
            jpgFlag=True
            file_name=download.downloader(_data['img_url'],illuster_name,illust_title+'_p'+str(counter),str(Iid)+'.jpg')
            print('===>'+file_name+' download completed!')
            print()
        
        _data=url.get_whole_url(session,base_url,str(counter),'.png')
        if _data['status_code'] != 200:
            pngFlag=False
        else:
            pngFlag=True
            file_name=download.downloader(_data['img_url'],illuster_name,illust_title+'_p'+str(counter),str(Iid)+'.png')
            print('===>'+illuster_name+':'+file_name+' download completed!')
            print()
        counter+=1

def run_by_iname(M,cookie,illuster):
    counter=1
    params={
        'id': illuster,
        'page': 1,
        'type': illuster,
    }
#    print(cookie)
    data=url.get_illusts(cookie,params) # list status_code cookie
    if data['status_code'] != 200:
        print ('▷-▷-▷>Something Wrong!')
        return
    illust_list=data['list']
    session=requests.Session()
    cookie=data['cookie']
    session.cookies=cookie
    print ()
    illustor_name=''
    num=0
    for d in illust_list:
        num+=1
        if num == 1:
            illustor_name=profile.get_person_name(session, illuster)
    print("""--------------------------
||Illustor Name:     %s
||Illustor ID:       %s
||Number of illusts: %s
--------------------------
""" % (illustor_name,illuster,str(num)))
    Max=input("How many illusts do you want to download? ")
    Max=int(Max)
    cookie=reload()
    session.cookies=cookie
    for d in illust_list:
        if counter > Max:
            break
        if d is '':
            print ('▷-▷-▷>sorry we can not download GIT image now QAQ')
            continue
        print ('=('+str(counter)+'/'+str(Max)+') Downloading...')
        run_by_iid(session,int(d))
        counter+=1
class manager(object):
    COOKIE={'a':None,'b':None}
    def title(self):
        print ("-▷-▷-▷-▷-▷-▷-▷-▷-▷-▷-▷-▷-▷-▷-▷-▷-▷-▷-▷")
        print ("WELCOME TO USE PIXIV ILLUST DOWNLOADER")
        print ("=====================================>")
    def run(self):
        while True:
            type=input("""what kind of service do you want?
            ===>1. Download illust by illust ID,
            ===>2. Download all illusts by illuster ID
            ===>3. **Quit**
        (1/2/3):""")
            if type == '1':
                cookie=reload()
                print ('    =========================')
                print ('===>load cookie successfully!')
                session=requests.Session()
                session.cookies=cookie
                while True:
                    Iid=input("Illust ID: ")
                    run_by_iid(session,Iid)
                    Continue=input('Do you want download next illust?(Y/N) ')
                    if Continue is 'N' or Continue is 'n':
                        break
            if type == '2':
                cookie=signin()
                while True:
                    Iid=input("Illuster ID: ")
                    print (Iid, str(Iid))
                    run_by_iname(self,cookie,Iid)
                    Continue=input('Do you want download next illuster?(Y/N) ')
                    if Continue is 'N' or Continue is 'n':
                        break
                    cookie=self.COOKIE
            if type == '3':
                break


if __name__ == '__main__':
    Maneger=manager()
    Maneger.title()
    Maneger.run()
    os.system('rm -rf __pycache__/')
