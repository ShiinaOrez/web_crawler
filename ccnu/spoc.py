import requests

url = "http://spoc.ccnu.edu.cn/"
check = "http://spoc.ccnu.edu.cn/userLoginController/userLogin"

headers = {
    "Host": "spoc.ccnu.edu.cn",
    "Connection": "keep-alive",
    "Content-Length": "40",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Origin": "http://spoc.ccnu.edu.cn",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "http://spoc.ccnu.edu.cn/starmoocHomepage",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": None
}

payload = {
    "loginName": "2017211712",
    "password": "password"
}

session = requests.Session()
# response = session.get(url, headers = headers)
response = session.post(check, data = payload, headers=headers)
print (response.__dict__)
