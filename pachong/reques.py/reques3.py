#coding=utf-8
import requests

#发送请求
# response = requests.get("https://www.baidu.com/img/bd_logo1.png")
#保存
# with open("a.png","wb") as f:
#     f.write(response.content)


response = requests.get("https://www.baidu.com")
print(response.status_code)
print(response.headers)
print(response.request.headers)
print(response.url)
print(response.request.url)
#因为浏览器知道你这不是常规的访问，所以只返回部分数据
print(len( response.content.decode() ))
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
response = requests.get("https://www.baidu.com",headers=headers)
print(len( response.content.decode() ))
print(response.content.decode() )

