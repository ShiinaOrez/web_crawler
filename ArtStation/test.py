import requests

headers = {
    "origin": "www.artstation.com",
    "referer": "www.artstation.com",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
}

response = requests.get('https://www.artstation.com/projects/nrLxX.json', headers = headers)

print (response)
for image in response.json().get('assets'):
    print (image.get('image_url'))
