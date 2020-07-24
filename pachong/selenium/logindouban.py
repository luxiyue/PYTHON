from selenium import webdriver
import time

if __name__ == '__main__':
    chrome_driver = 'E:\\chromedriver_win32\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path = chrome_driver)
    driver.get('https://www.douban.com/')

    driver.switch_to_frame(0)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()

    driver.find_element_by_xpath('//*[@id="username"]').send_keys('15507253909')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('luzelong1124')
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
    print(driver.page_source)
