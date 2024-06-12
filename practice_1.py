# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

# 送出 Get 請求 (http://httpbin.org/)
r = requests.get("https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&kwop=7&keyword=%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90&area=6001001000%2C6001002000%2C6001016000&order=15&asc=0&page=2&mode=l&jobsource=2018indexpoc")
print(r.status_code)

# 以判斷式判定 Get 請求是否成功
r = requests.get("https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007000000&kwop=7&keyword=%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90&area=6001001000%2C6001002000%2C6001016000&order=15&asc=0&page=2&mode=l&jobsource=2018indexpoc")
if r.status_code == 200:
    print("請求成功...")
else:
    print("請求失敗...")

# 含有參數的 Get 請求 (Decode url)
import requests
url_params = {'keyword' : '資料分析', 'area' : '6001001000,6001002000,6001016000'} # area 中，每個數字代表一特定區域。 # dictionary 格式
r = requests.get("https://www.104.com.tw/jobs/search/", params = url_params)
print(r.url)

# 顯示回應字串
print(r.text)

# 送出 Post 請求
import requests
post_data = {'keyword' : '資料分析', 'area' : '6001001000,6001002000,6001016000'} # 與前述 url_params 相同。
r = requests.get("https://www.104.com.tw/jobs/search/", params = url_params)
print(r.text)

# 取得 HTTP 回應內容
r = requests.get("https://www.104.com.tw/jobs/search/", params = url_params) # 變數 r 為回應內容的 Response 物件，其中包含許多屬性資料。
print(r.encoding)
print(r.content)
print(r.raw)

r = requests.get("https://www.104.com.tw/jobs/search/", params = url_params, stream = True)
print(r.raw.read(15))

# 取得 JSON 回應
r = requests.get("http://httpbin.org/user-agent")
print(r.text)
print(type(r.text))
print("----------------------")

print(r.json())
print(type(r.json()))

# 查詢回應狀態碼的進一步訊息
print(r.status_code)
print(r.raise_for_status())

# 取得回應的 HTTP 標頭資訊
r = requests.get("https://www.104.com.tw/jobs/search/", params = url_params, stream = True)
print(r.headers["Content-Type"])
#print(r.headers["Content-Length"])   # 出現 error
print(r.headers["Date"])
#print(r.headers["Server"])            # 出現 error

print(r.headers.get('Content-Type'))
print(r.headers.get('Content-Length'))   # 顯示 none
print(r.headers.get('Date'))
print(r.headers.get('Server'))           # 顯示 none

# cookie
import requests
url_params = {'keyword' : '資料分析', 'area' : '6001001000,6001002000,6001016000'}
r = requests.get("https://www.104.com.tw/jobs/search/", params = url_params)
print(r.url)
print(r.cookies)

# 為避免網站封鎖，更改 user-agent 標頭資訊
import requests
url = "http://httpbin.org/user-agent"
r = requests.get(url)
print(r.text)
print("================================")

url_headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

r = requests.get(url,headers = url_headers)
print(r.text)

# 











