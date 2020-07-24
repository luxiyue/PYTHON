from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

if __name__ == '__main__':
    chrome_driver = 'E:\\chromedriver_win32\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path = chrome_driver)
    driver.get('https://image.baidu.com/')
    driver.find_element_by_id('kw').send_keys('美女')
    driver.find_element_by_class_name('s_search').click()
    a = driver.find_element_by_xpath('//*[@id="imgid"]/div/ul/li[1]/div/a/img')
    action = ActionChains(driver).move_to_element(a)
    #ActionChains(driver).context_click(a).perform()
    action.context_click(a)
    action.perform()#执行保存

    #time.sleep(3)
    #driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')  滚轮向下滑动



    
