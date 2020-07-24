import requests


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
           "Cookie":'ll="118263"; bid=dy7qfE5rPdQ; _pk_ses.100001.8cb4=*; __utma=30149280.338987838.1591836487.1591836487.1591836487.1; __utmc=30149280; __utmz=30149280.1591836487.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; dbcl2="215984922:aqvGkLs7IJM"; ck=c4j9; _pk_id.100001.8cb4=15a0803f35dc181f.1591836486.1.1591836487.1591836486.; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.21598; __utmb=30149280.3.10.1591836487; __yadk_uid=pMVzuuyl03QqUOLfwwJRWW0bcCPso7kl'}
url="https://www.douban.com/"
a=requests.get(url,headers=headers)
print(a.content.decode())


