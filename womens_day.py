import requests

url='https://web.wutnews.net/lucky/index/change'

response=requests.get(url)

print (response.text)
