import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib import font_manager

allUniv = []
x = []
y = []
#获取指定网址的页面源码
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""

#筛选出网页中《td》标签中的信息，并存放到列表allUniv中
def fillUnivList(soup):
    data = soup.find_all('tr')#data类型是bs4.element.ResultSet
    for tr in data:
        # print(tr)
        ltd = tr.find_all('td')#类型是bs4.element.ResultSet
        if len(ltd)==0:
            continue
        singleUniv = []
        for td in ltd:
            # print(td.string)
            singleUniv.append(td.string)
        allUniv.append(singleUniv)

#控制台打印结果
def printUnivList(num):
    print("{:<6}{:<30}{:<40}{:<8}".format("年度排名","历史排名","电影名称","上映年份"))
    for i in range(num):
        u=allUniv[i]
        print("{:<6}{:<30}{:<40}{:<8}".format(u[0],u[1],u[2],u[6]))

#将电影名称，历史排名放到x,y列表
def fix(num):
    for i in range(num):
        u = allUniv[i]
        x.append(u[2])
        y.append(u[1])

def draw():
    my_font = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/MSYH.ttc")
    #设置图片大小
    plt.figure(figsize=(20, 15), dpi=80)
    #画柱状图
    # plt.bar(range(len(x)),y,width=0.3)
    #画横向柱状图
    plt.barh(range(len(x)), y, height=0.3,color="orange")
    #设置x轴刻度和字样
    plt.yticks(range(len(x)),x,fontproperties=my_font)
    # 添加描述信息
    plt.xlabel("历史排名", fontproperties=my_font)
    plt.ylabel("电影名称", fontproperties=my_font)
    plt.title("2020最火的电影排行", fontproperties=my_font)
    # 绘制网格
    plt.grid(alpha=0.3)  # 里面的第一个参数设置透明度
    #展示
    plt.show()

def main():
    url = 'http://58921.com/alltime/2020'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillUnivList(soup)
    printUnivList(20)
    fix(20)
    draw()


if __name__ == '__main__':
    main()