import login,url,download
import os

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

# get Illust ID
while True:
    Iid=input("Illust ID:")
    url_and_title=url.get_base_url(session,Iid)

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
    
    Continue=input('Do you want download next illust?(Y/N)')
    if Continue is 'N' or Continue is 'n':
        break

os.system('rm -rf __pycache__/')