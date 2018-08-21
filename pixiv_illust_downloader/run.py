import login,url,download
import os

def run_by_iid(session,Iid):
# get Illust ID
    url_and_title=url.get_base_url(session,Iid)
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
        _data=url.get_whole_url(session,base_url,str(counter),'.jpg')
        if _data['status_code'] != 200:
            jpgFlag=False
        else:
            jpgFlag=True
            file_name=download.downloader(_data['img_url'],illuster_name,illust_title+'_p'+str(counter),str(Iid)+'.jpg')
            print(file_name+' download completed!')
        
        _data=url.get_whole_url(session,base_url,str(counter),'.png')
        if _data['status_code'] != 200:
            pngFlag=False
        else:
            pngFlag=True
            file_name=download.downloader(_data['img_url'],illuster_name,illust_title+'_p'+str(counter),str(Iid)+'.png')
            print(illuster_name+':'+file_name+' download completed!')
        counter+=1

def run_by_iname(session,illuster):
#    url.test(session,illuster,base_url)
#    counter=1
#    while True:
    params={
        'id': illuster,
        'page': 1,
        'type': illuster,
    }
    data=url.get_illusts(session,params)
#    if data['status_code'] != 200:
#        break
#        counter+=1
    illust_list=data['list']
    for id in illust_list:
        run_by_iid(session,id)

class manager(object):
    def run(self):
        try:
            re=login.reload()
            if re['code']:
                session=re['session']
                print ('load cookie successfully!')
            else:
                e=None.a
        except:
            username=input("your pixiv account: ")
            password=input("your pixiv password: ")

            # get have cookies requests.Session()
            session=login.login(username,password)

            print('login successfully!')

        while True:
            type=input("""what kind of service do you want?
            1. Download illust by illust ID,
            2. Download all illusts by illuster ID
            3. Quit
        (1/2/3):""")
            if type == '1':
                while True:
                    Iid=input("Illust ID:")
                    run_by_iid(session,Iid)
                    Continue=input('Do you want download next illust?(Y/N)')
                    if Continue is 'N' or Continue is 'n':
                        break
            if type == '2':
                while True:
                    Iid=input("Illuster ID:")
                    run_by_iname(session,Iid)
                    Continue=input('Do you want download next illuster?(Y/N)')
                    if Continue is 'N' or Continue is 'n':
                        break
            if type == '3':
                break


if __name__ == '__main__':
    Maneger=manager()
    Maneger.run()
    os.system('rm -rf __pycache__/')