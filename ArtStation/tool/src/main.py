import requests
import os
import re
import json
from setting import pre_data_url, tail_data_url, headers, project_url, _printTab1

failList = list([])

class User(object):
    """ user on artstation initalize by profile link """
    username = None
    ill_count = None
    pages = None
    data = None

    def __init__(self,link):
        illustor_name = link.replace('https://www.artstation.com/','')
        self.username = illustor_name
        j = pre_data_url + illustor_name + tail_data_url
        session = requests.Session()
        data = list([])
        response = session.get(j+"1", headers = headers)
        count = response.json().get('total_count')
        self.ill_count = count
        pages = count//50
        if count%50 != 0:
            pages+=1
        self.pages = pages
        for i in range(pages):
            response = session.get(j+str(i+1), headers = headers)
            if response.json().get('data') is None:
                continue
            for re in response.json().get('data'):
                data.append(re)
        self.data = data
    
    def download(self, isAll, basedir):
        print (_printTab1*2,"|"+self.username+" have "+ str(self.ill_count) + ' illusts')
        number = self.ill_count
        if not isAll:
            number = int(input(_printTab1*2+' |how many illusts you want to download to your computer?'))
        for seg in zip(range(number), self.data):
            tot = seg[0] + 1
            print(_printTab1*3,'('+str(tot)+'/'+str(number)+')__')
            project = Project(seg[1])
            path=basedir+'/Images/'+self.username+'/'
            project.download(path)

class Project(object):
    """ Project """

    hash_id = None
    user_id = None
    assertList = None
    title = None

    def __init__(self,data):
        if data.get('title') is not None:
            self.title = data.get('title')
            self.hash_id = data.get('hash_id')
            self.user_id = data.get('user_id')
            downloadList=list([])
            assert_json_url = project_url+self.hash_id+'.json'
            session = requests.Session()
            response = session.get(assert_json_url, headers = headers)
            for image in response.json().get('assets'):
                if image.get('has_embedded_player') is False:
                    downloadList.append(image.get('image_url'))
            self.assertList = downloadList
    
    def download(self, file_path):
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        num = 0
        for downloadLink in self.assertList:
            image = Image(downloadLink)
            image.download(file_path+self.title+"_"+self.hash_id,
                           self.title+"_"+self.hash_id, 
                           num)
            num += 1
                
class Image(object):
    """ Image """
    downloadLink = None

    def __init__(self, link):
        self.downloadLink = link
    
    def makeSureTail(self):
        tail = '.png'
        if 'jpg' in self.downloadLink:
            tail = '.jpg'
        if '.gif' in self.downloadLink:
            tail = '.gif'
        return tail

    def download(self, file_name, name, num):
        tail = self.makeSureTail()
        file_name=file_name+'_'+str(num)+tail
        file_name = checkChar(file_name)
        if os.path.isfile(file_name): 
            print (_printTab1*4,'>Image already exist = =')
            return
        r=requests.get(self.downloadLink, headers=headers, allow_redirects=True)
        try:
            open(file_name, 'wb').write(r.content)
        except:
            print(_printTab1*3, "WARNNING: SOMETHING MISTAKE")
            failList.append(self.downloadLink)
        s = name+'_'+str(num)+tail+' download successfully!'
        printList = cut_text(s,41)
        for ss in printList:
            print(_printTab1*4, "|"+ss)

def cut_text(text,lenth):
    textArr = re.findall('.{'+str(lenth)+'}', text)
    textArr.append(text[(len(textArr)*lenth):])
    return textArr

def getLinkList():
    linkList = list([])
    while True:
        url = input("|Input Link('*' to *STOP*): ")
        if url is "*":
            break
        else:
            linkList.append(url)
    return linkList

def checkMode():
    check_mode = input("|Mode: Download All('Y/N'): ")
    isAll = False
    if ('y' in check_mode) or ('Y' in check_mode):
        isAll = True
    return isAll

def checkChar(file_name):
    charList = list(["'",'"',"\\","/","<",">","?","*","|"])
    for char in charList:
        file_name.replace(char,"")
    return file_name

def printFail():
    print("|--*Fail List*--")
    if failList == list([]):
        print("| All Successful!")
    else:
        for seg in zip(range(999),failList):
            print("|("+str(seg[0]+1)+"/"+str(len(failList))+"): "+seg[1])
    print("|")
    return 

def _main(basedir):
    linkList = getLinkList()
    isAll = checkMode() 

    main_num = len(linkList)
    i = 0
    for link in linkList:
        print(_printTab1, "|("+str(i+1)+"/"+str(main_num)+")"+"Download Misstion Start:")
        user = User(link)
        user.download(isAll, basedir)
        i += 1
        print(_printTab1*2,'----WORK IS DONE!!----')
        print()
        printFail()
