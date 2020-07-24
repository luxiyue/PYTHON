from selenium import webdriver
import time

if __name__ == '__main__':
    chrome_driver = 'E:\\chromedriver_win32\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path = chrome_driver)
    driver.get('https://www.douban.com/')

    #1通过标签的id值获取标签
    ret1 = driver.find_element_by_id('anony-nav')
    print(ret1)
    #2通过标签的id值获取多个标签
    ret2 = driver.find_elements_by_id('anony-nav')
    print(ret2)
    #3通过标签的class属性值获取标签
    ret3 = driver.find_elements_by_class_name('anony-nav-links')
    print(ret3)
    #4通过xpath获取左上角豆瓣图片的《a》标签
    ret4 = driver.find_elements_by_xpath('//*[@id="anony-nav"]/h1/a')
    print(ret4)
    #5通过标签包裹的文本'下载豆瓣 App'获取元素列表（精确定位）
    ret5 = driver.find_element_by_link_text('下载豆瓣 App')
    print(ret5)
    #6通过标签包裹的文本“豆瓣”，获取元素的列表（模糊定位）
    ret6 = driver.find_elements_by_partial_link_text('豆瓣')
    print(len(ret6))
    #7通过标签名获取元素列表
    ret7 = driver.find_elements_by_tag_name('div')
    print(len(ret7))
    #8获取<h1>标签包裹的文本内容
    ret8 = driver.find_element_by_tag_name('h1')
    print(ret8.text)
    #9通过标签包裹的文本‘下载豆瓣 App’获取其href属性值
    ret9 = driver.find_element_by_link_text('下载豆瓣 App')
    print(ret9.get_attribute('href'))





