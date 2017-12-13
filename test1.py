import urllib.request
import json
import urllib.parse
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
input_data = input("输入你要翻译的数据：")
data = {}
#head 添加请求头部，如果服务端通过请求头判断是否为机器访问，可以通过添加请求头
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
head['Accept'] = 'application/json, text/javascript, */*; q=0.01'

data['type'] = 'AUTO'
data['i'] = input_data
data['doctype'] = 'json'
data['xmlVersion'] = '1.8'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')
# req = urllib.request.urlopen(url,data,head)  加了header 直接用urlopen会报错
req = urllib.request.Request(url,data,head)
"""
或者通过add_header()添加请求头部
req = urllib.request.Request(url,data)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0')
"""
req = urllib.request.urlopen(req)
re_data = req.read().decode('utf-8')
re_data = json.loads(re_data)
re = re_data['translateResult'][0][0]['tgt']
exit(re)