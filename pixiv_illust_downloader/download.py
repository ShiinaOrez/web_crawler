import login
import os
import requests

basedir=os.path.abspath(os.path.dirname(__file__))
headers = login.headers

def downloader(url,illustor_name,name,tail):
    # url : string : download url
    # illlustor_name : string : illustor's nick name
    # name : string : illust's title
    # tail : string : ".jpg" or ".png"

    headers['Referer'] = url

    ''' mkdir and make sure illust '''
    file_path=basedir+'/Images/'+illustor_name+'/'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_name=file_path+name+'_'+tail
    if os.path.isfile(file_name): 
        print ('▷-▷-▷>Image already exist = =')
        return name+'_'+tail

    ''' download and save the illust '''
    r=requests.get(url, headers=headers, allow_redirects=True)
    open(file_name, 'wb').write(r.content)
    return name+'_'+tail
