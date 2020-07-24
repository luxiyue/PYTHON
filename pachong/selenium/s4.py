from selenium import webdriver
import time

if __name__ == '__main__':
    chrome_driver = 'E:\\chromedriver_win32\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path = chrome_driver)
    driver.get('https://www.douban.com/')
    driver.find_element_by_xpath('//*[@id="anony-sns"]/div/div[3]/div/div[1]/ul/li[1]/div/a/img').click()
    time.sleep(2)
    driver.back()#页面回退
    time.sleep(2)
    driver.forward()#页面前进
