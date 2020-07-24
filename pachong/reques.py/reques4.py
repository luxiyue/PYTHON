import requests

#使用代理ip
proxies = {"http":"http://123.57.76.102:80"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
p = {"wd":"美女"}
url_temp = "https://www.baidu.com/s?"#后面的问号可有可无

r = requests.get(url_temp,headers=headers,params=p,proxies=proxies)
print(r.status_code)
print(r.request.url)
