import requests
import os
import json

basedir=os.path.abspath(os.path.dirname(__file__))

url = input("The illustor you want to know?[URL]")
illustor_name = url.replace('https://www.artstation.com/','')
j = 'https://www.artstation.com/users/' + illustor_name + '/projects.json?page='

project_url = "https://www.artstation.com/projects/"

# url = 'https://www.artstation.com/timbougami'
# j = 'https://www.artstation.com/users/timbougami/projects.json?page=1'

headers = {
    "origin": "https://www.artstation.com",
    "referer": "https://www.artstation.com",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
}

session = requests.Session()
data = list([])

response = session.get(j+"1", headers = headers)
count = response.json().get('total_count')
pages = count//50
if count%50 != 0:
    pages+=1
print (illustor_name+" have "+ str(count) + ' illusts')
number = int(input('how many illusts you want to download to your computer?'))
for i in range(pages):
    response = session.get(j+str(i+1), headers = headers)
    if response.json().get('data') is None:
        continue
    for re in response.json().get('data'):
        data.append(re)
        
tot = 1
for illust in data:
    if tot > number:
        print('WORK IS DONE!!')
        break
    print('('+str(tot)+'/'+str(number)+')')
    tot += 1
    if illust.get('title') is not None:
        cover = illust.get('cover')
        hash_id = illust.get('hash_id')
        illuster_id = illust.get('user_id')
        isImage=True
        downloadList=list([])
        assert_json_url = project_url+hash_id+'.json'
        response = session.get(assert_json_url, headers = headers)
        for image in response.json().get('assets'):
            large_url = image.get('image_url')
            if image.get('has_embedded_player') is False:
                downloadList.append(image.get('image_url'))
        file_path=basedir+'\\Images\\'+illustor_name+'\\'
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        num=-1
        for downloadLink in downloadList:
            num+=1
            headers['referer'] = illust.get('permalink')
            name = illust.get('title')+illust.get('hash_id')
            tail = '.png'
            if 'jpg' in downloadLink:
                tail = '.jpg'
            if '.gif' in downloadLink:
                tail = '.gif'
            file_name=file_path+name+hash_id+'_'+str(num)+tail
            file_name = file_name.replace('"','')
            file_name = file_name.replace('/','')
            file_name = file_name.replace('"','')
#               print(file_name)
            if os.path.isfile(file_name): 
                print ('>Image already exist = =')
                continue

            r=requests.get(downloadLink, headers=headers, allow_redirects=True)
            open(file_name, 'wb').write(r.content)
            print (name+hash_id+'_'+str(num)+tail+' download successfully!')
