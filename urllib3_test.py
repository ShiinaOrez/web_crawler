from urllib import request

import json

import urllib3

http=urllib3.PoolManager()
#实例化PoolManager
'''
proxy=request.ProxyHandler({"http":"localhost:9999"})

opener=request.build_opener(proxy,request.HTTPHandler)

request.install_opener(opener)
'''
'''
encoded_args=urlencode({'arg':'value'})

url='http://httpbin.org/post?'+encoded_args

response=http.request('POST',url)
#对于POST和PUT请求，需要手动的编码查询参数
'''
'''
#提交表单数据
response=http.request('POST','http://httpbin.org/post',field={'field':'value'})
#可以直接写在field参数里面
'''
'''
#发送JSON给服务器
data={'attribute':'value'}
encoded_data=json.dumps(data).encode('utf-8')
response-http.request('POST','http://httpbin.org/post',body=encoded_data,headers={'Content-Type':'application/json'})
#将需要发送的json数据编码后传递给request()的body参数，然后在请求头中设置Content-Type字段为application/json
'''
response=http.request('GET',"http://www.baidu.com",headers={'X-something':'value'})
#调用request发起请求，返回一个HttpResponse对象,并且设置请求头
header=response.headers
#响应头
h=str(header)

statu=response.status
#响应的状态码
s=str(statu)

data=response.data.decode("utf-8")
#响应的数据
d=str(data)

with open("baidu/baidu_headers.txt","w") as f:
	f.write(h)

#f=open("baidu/baidu_status.txt","w")

#f.wirte(s)

#close(f)

with open("baidu/baidu_data.html","w") as f:
	f.write(d)
