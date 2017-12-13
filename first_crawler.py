#import urllib.request
from urllib import request

proxy=request.ProxyHandler({"http":"localhost:9999"})

opener=request.build_opener(proxy,request.HTTPHandler)

request.install_opener(opener)

headers=[("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"),
	("User-Agent","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36")]

req=request.Request("https://github.com")

req.add_header(headers,[("shiina"),("orez")])

data=request.urlopen(req).read()

'''sourceUrl="http://r.photo.store.qq.com/psb?/V13Gxo2x1UzVE2/zn3KXCK0XgcGFulnDT5.Ukmgx8YtCfFfpIJPf1vRoUM!/r/dPMAAAAAAAAA"
quoteUrl=request.quote(sourceUrl)
print (quoteUrl)'''

file=request.urlopen("https://github.com")

myfirstpage=file.read().decode("utf-8")

with open("myfirstpage.html","w") as f:
	f.write(myfirstpage)
