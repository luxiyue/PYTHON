# -*- coding: utf-8 -*-
'''
Created on Thu Jul  5 20:48:25 2018
@author: brave-man
blog: http://www.cnblogs.com/zrmw/
python3 + anaconda（Spyder） + resquests + BeautifulSoup
'''

import requests
from bs4 import BeautifulSoup
# from termcolor import colored

# 控制台输出文本颜色控制，网络不太好，没有安装termcolor，不过在公司测试过，函数传参应该没有问题
# print(colored("abc", "red"))

# 通过requests库中的get方法获取整个响应页面，存放在res中
res = requests.get("https://www.cnblogs.com/zdong0103/p/8492779.html")
# (1) res.encoding = "utf-8"
soup = BeautifulSoup(res.text, "html.parser")
# 这时候如果打印的soup的话，会在控制台中输出整个响应页面的源代码
#print(soup)
# 如果打印的是乱码，则可以在 (1) 处添加 (1) 所示代码，设置编码格式，不过有时候是不需要的。

# 接下来对网页的源码进行剖析
""" 
操作如下：
在网页中按 F12 查看网页源代码，文章标题在 class = "block_title" 里面,
soup.select(".block_title") 获取的是一个列表，获取此列表的第一个元素，
所以 index = 0 ， 从标签中获取文本一般使用 text 方法即可
同上，正文在 class = "blogpost-body"


"""
title = soup.select(".block_title")[0].text
texts = soup.select(".blogpost-body")[0].text
time = soup.select(".itemdesc span")[0].text
author = soup.select("#header")[0].text

print(title, author, time, texts)
