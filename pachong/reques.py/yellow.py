import requests
from bs4 import BeautifulSoup

app=[]
old=[]
driver = requests.get("http://www.nhy5.com/Wzlist/jiqingxiaoshuo.html")
html = driver.content.decode()
soup = BeautifulSoup(html, "html.parser")
data = soup.find_all('ul')

for i in data:
    ltd = i.find_all('li')
    for j in ltd:
        k = j.find_all('a')
        if len(k)!=0:
            app.append(str(k))
for i in app:
    findex = i.index("href")
    eindex = i.rfind('"')
    b = i[findex+6:eindex]
    old.append("http://www.nhy5.com/"+b)


for i in old:
    print(i)
    # response = requests.get(i)
    # html1 = response.content.decode()
    # soup1 = BeautifulSoup(html1, "html.parser")
    # data = soup.find_all('h1')
    # for o in data:
    #     ww = soup.find_all('p')
    #     print(ww)
    # if i==1:
    #     break
