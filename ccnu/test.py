import requests
import werkzeug

scheme = "http://"
domain = "self.ccnu.edu.cn:8080"
path = "/Self/login/"
url = scheme + domain + path
n = input("username: ")
p = input("password: ")

payload = {
    "foo": n,
    "bar": p,
    "checkcode": None,
    "account": n,
    "password": p,
    "code": None
}
header = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Cookie": None,
    "Host": "self.ccnu.edu.cn:8080",
    "Referer": "http://self.ccnu.edu.cn:8080/Self/login/",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
session = requests.Session()
response = session.get(url, headers = header)
index = response.headers['Set-Cookie'].find(";")
url = url + ";" + response.headers['Set-Cookie'][:index].lower()
# index = response.text.find("checkcode")
# payload["checkcode"] = response.text[index+18:index+22]
print (url)
response = session.post(url, data=payload)
for s in response.__dict__["url"].split(";"):
    if "session" in s:
        header["Cookie"] = s
response = session.post(url, data = payload, headers = header)
# print (response.__dict__)

'''
url = response.url

response = requests.post(url, data = payload, headers = header)
setcookie = response.headers['Set-Cookie']
cookie_dict = werkzeug.http.parse_cookie(setcookie)
JSESSIONID = cookie_dict['JSESSIONID']
fmt = "JSESSIONID={}"
header['Cookie'] = fmt.format(JSESSIONID)

response = requests.get(scheme+domain+path)
'''
for key in response.__dict__.keys():
    if key[0] == '_':
        continue
    print (key, response.__dict__[key])

