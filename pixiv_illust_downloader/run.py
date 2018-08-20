import login,url,download

username=input("your pixiv account: ")
password=input("your pixiv password: ")

# get have cookies requests.Session()
session=login.login(username,password)
print('login successfully!')

# get Illust ID
while True:
    Iid=input("Illust ID:")
    base_url=url.get_base_url(session,Iid)
    counter=0
    jpgFlag=True
    pngFlag=True
    while jpgFlag or pngFlag:
        _data=url.get_whole_url(session,base_url,str(counter),'.jpg')
        if _data['status_code'] != 200:
            jpgFlag=False
        else:
            jpgFlag=True
            file_name=download.downloader(_data['img_url'],'.jpg')
            print(file_name+' download completed!')
        
        _data=url.get_whole_url(session,base_url,str(counter),'.png')
        if _data['status_code'] != 200:
            pngFlag=False
        else:
            pngFlag=True
            file_name=download.downloader(_data['img_url'],'.png')
            print(file_name+' download completed!')
        counter+=1
    
    Continue=input('Do you want download next illust?(Y/N)')
    if Continue is 'N' or 'n':
        break