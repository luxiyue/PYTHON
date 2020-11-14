from selenium import webdriver
import requests



def looking(mubiao):
    chrome_driver = 'E:\\chromedriver_win32\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path = chrome_driver)
    driver.get('https://image.baidu.com/')
    driver.find_element_by_id('kw').send_keys(mubiao)
    driver.find_element_by_class_name('s_newBtn').click()
    href = driver.find_element_by_name("pn0").get_attribute('href')
    print(href)
    return href
    driver.close()

def download(url,n):
    chrome_driver = 'E:\\chromedriver_win32\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path = chrome_driver)
    driver.get(url)
    for i in range(n):
        ret = driver.find_element_by_class_name("currentImg").get_attribute("src")
        response = requests.get(ret)
        with open(r'E:\Photo\%s.jpg' % (i+1),'wb') as f:
            print("第",i+1,"张图片下载完毕！！！")
            f.write(response.content)
        driver.find_element_by_xpath('//*[@id="container"]/span[2]/span').click()
    driver.close()

if __name__== "__main__":
    mubiao = input("请输入要下载的图片类型：")
    n = int(input("请输入下载数量："))
    url = looking(mubiao)
    download(url,n)