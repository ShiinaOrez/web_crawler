import os
import requests
import execjs
import json
import xlwt
import xlrd

def createParams(city, month, ctx):
    '''由城市名、年月得出经js加密后的post参数,ctx由js代码解析得到'''
    method = 'GETDAYDATA'
    js = 'getEncryptedData("{0}", "{1}", "{2}")'.format(method, city, month)
    params = ctx.eval(js)
    return {'hd': params}


def getResponseData(city, month, ctx):
    '''由城市名、年月向服务器发送post请求并解密返回数据,ctx由js代码解析得到'''
    apiUrl = 'https://www.aqistudy.cn/historydata/api/historyapi.php'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }

    response = requests.post(apiUrl, data=createParams(city, month, ctx), headers=headers, timeout=10)
    if response.status_code != 200:
        return None
    # 解析数据
    js = 'decodeData("{0}")'.format(response.text)
    decrypted_data = ctx.eval(js)
    data = json.loads(decrypted_data)
    return data['result']['data']['items']


def new_excel(city, year, month, items):
    filename=xlwt.Workbook()  
    ws=filename.add_sheet("1") 
    for i, item in enumerate(items):
        ws.write(i+1, 0, item['time_point'])
        ws.write(i+1, 1, item['aqi'])
        ws.write(i+1, 2, item['pm2_5'])
        ws.write(i+1, 3, item['pm10'])
        ws.write(i+1, 4, item['so2'])
        ws.write(i+1, 5, item['no2'])
        ws.write(i+1, 6, item['co'])
        ws.write(i+1, 7, item['o3'])
        ws.write(i+1, 8, item['quality'])
    filename.save(os.getcwd() + '\\' + city + '\\' + str(year) + "-" + str(month).zfill(2) + '.xls')


def new_xls(aqi):
    filename=xlwt.Workbook()  
    ws=filename.add_sheet("1") 
    for i, v in enumerate(aqi):
        ws.write(i+1, 0, v)
    filename.save('这是一个很棒的表.xls')    

if __name__ == '__main__':
    # js环境，这里用nodeJS
    node = execjs.get()
    # compile javascript
    ctx = node.compile(open('encryption.js', encoding='utf-8').read())

    city = input('请输入城市名(如: 上海)：')
    year_start = int(input('请输入开始年份(如: 2014)：'))
    month_start = int(input('请输入开始月份(如: 5)：'))
    year_end = int(input('请输入结束年份(如: 2019)：'))
    month_end = int(input('请输入结束月份(如: 5)：'))

    folder = os.getcwd() + '\\' + city
    print(folder)
    if not os.path.exists(folder):
        os.makedirs(folder)  
        print("-->新建文件夹: {}".format(city))

    aqi_aver = []
    for year in range(year_start, year_end+1):
        for month in range(month_start, 13):
            if year == year_end and month == month_end:
                break
            items = getResponseData(city, str(year) + str(month).zfill(2), ctx)
            if not items:
                print("Failed.")
            else:
                new_excel(city, year, month, items)
                l = len(items)
                count = 0
                for item in items:
                    if isinstance(item['aqi'], str):
                        count += int(item['aqi'])
                    else:
                        count += item['aqi']
                count /= l
                print("{}-{}: {}".format(year, str(month).zfill(2), count))
                aqi_aver.append(count)
        month_start = 1
    new_xls(aqi_aver)