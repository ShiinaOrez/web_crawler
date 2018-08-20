import login
import urllib.request

headers=login.headers

def downloader(url,num,tail):
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-Agent',headers['User-Agent']),
        ('Referer',url),
    ]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url,'TEST'+num+tail)
    return 'TEST'+tail