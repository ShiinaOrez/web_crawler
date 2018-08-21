import login
import urllib.request
import os

headers=login.headers
basedir=os.path.abspath(os.path.dirname(__file__))

def downloader(url,illuster_name,name,tail):
    file_path=basedir+'/Images/'+illuster_name+'/'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_name=file_path+name+'_'+tail
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-Agent',headers['User-Agent']),
        ('Referer',url),
    ]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url,file_name)
    return name+'_'+tail