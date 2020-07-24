import requests
import json


# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
# data = {
# "from": "zh",
# "to": "en",
# "query": "可以",
# "simple_means_flag": "3",
# "sign": "515402.212603",
# "token": "4c52ebc2fd09a84822b434334b8ac816",
# "domain": "common"
# }
# post_url="https://fanyi.baidu.com/v2transapi"
# r = requests.post(post_url,data=data,headers=headers)
# print(r.content.decode())

# 上面是网页端的  发现请求有js限制
# headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Mobile Safari/537.36"}
#
# post_data = {
# "query": "我长得很帅",
# "from": "zh",
# "to": "en",
# "token": "4c52ebc2fd09a84822b434334b8ac816",
# "sign":"955239.684118",
# }
# post_url="https://fanyi.baidu.com/basetrans"
# r = requests.post(post_url,data=post_data,headers=headers)
# print(r.content.decode())
# dirt_ret = json.loads(r.content.decode())
# ret = dirt_ret["trans"][0]["dst"]
# print(ret)


#我发现上面的方法，并不能爬取了，下面的代码只能转化单词，不能转化句子
def transform(it):
    url = "https://fanyi.baidu.com/sug"
    # 定义请求的参数
    data = {'kw': it}
    # 创建请求， 发送请求， 爬取信息
    res = requests.post(url, data=data)
    # 解析结果
    str_json = res.content.decode("utf-8")
    # print(type(str_json))
    print(str_json)
    myjson = json.loads(str_json)
    # print(type(myjson))
    print(myjson['data'][0]['v'])

if __name__ == '__main__':
    u = input("请输入想要翻译的内容:")
    transform(u)