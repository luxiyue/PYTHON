from selenium import webdriver
import time

if __name__ == '__main__':
    '''
    切换窗口
    '''
    chrome_driver = 'E:\\chromedriver_win32\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path = chrome_driver)
    driver.get('https://www.douban.com/')
    driver.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[2]/a').click()

    #1.获取当前所有的窗口
    current_window = driver.window_handles
    print(current_window)
    driver.switch_to.window(current_window[0])#选择使用的当前窗口
