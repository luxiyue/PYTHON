from selenium import webdriver
import time

if __name__ == '__main__':
    #创建浏览器对象
    chrome_driver = 'E:\\chromedriver_win32\\chromedriver.exe'  #chromedriver的文件位置
    driver = webdriver.Chrome(executable_path = chrome_driver)
    #请求页面
    driver.get('https://www.baidu.com/')
    #页面的基本操作（找到页面的输入框id值，并输入关键字）
    driver.find_element_by_id('kw').send_keys('色逼')
    #找到按钮‘百度一下’的id，完成点击操作
    driver.find_element_by_id('su').click()
    #截屏操作
    #time.sleep(2)#延时两秒  方便截取屏幕的具体信息
    #driver.save_screenshot('baidu.png')

    
    print(driver.page_source)#获取页面渲染之后的数据
    print(driver.get_cookies())#获取页面的cookies
    print(driver.current_url)#查看当前的url路径

    time.sleep(5)
   # driver.close()#关闭页面
    #driver.quick()#关闭浏览器
    



