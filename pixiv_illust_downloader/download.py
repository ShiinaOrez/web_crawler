import login
#import urllib.request
import os
import requests

#headers=login.headers
basedir=os.path.abspath(os.path.dirname(__file__))

def downloader(url,illuster_name,name,tail):
    headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
        'Referer': url,
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
    file_path=basedir+'/Images/'+illuster_name+'/'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_name=file_path+name+'_'+tail
    if os.path.isfile('./'+name+tail): 
        print ('image already exist = =')
        return name+'_'+tail
#    opener = urllib.request.build_opener()
#    opener.addheaders = [
#        ('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'),
#        ('Referer',url),
#    ]
#    urllib.request.install_opener(opener)
#    urllib.request.urlretrieve(url,file_name)
    r=requests.get(url, headers=headers, allow_redirects=True)
    open(file_name, 'wb').write(r.content)
    return name+'_'+tail