import urllib3

http=urllib3.PoolManager()

response=http.request('GET',"http://www.baidu.com")

header=response.headers

h=header.read()

statu=response.status

s=statu.read()

data=response.data.decode("utf-8")

d=data.read().decode("utf-8")

with open("baidu_headers.txt","w") as f:
	f.write(h)

with open("baidu_status.txt","w") as f:
	f.wirte(s)

with open("baidu_data.html","w") as f:
	f.write(d)
