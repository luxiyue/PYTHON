
# 需要安装ChromeDriver与对应库，或者你学习后找到适合你的浏览器的驱动方法
# 或者寻找无界面浏览器PhantomJS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import random
import re
import time

def get_url(this_url,word):
	"""
	用于找到网页对应关键词的页面
	this_url : 首页搜索网址
	word :搜索的关键词
	return : 具体返回关键词所在的网页
	"""
	browser = webdriver.Chrome(executable_path =  'E:\\chromedriver_win32\\chromedriver.exe')
	browser.get(this_url)
	this_input = browser.find_element_by_id('kw')
	this_input.send_keys(word)	#将你的关键词输入到输入框中
	time.sleep(3)	#暂停三秒点击，为了检测，可不要
	button = browser.find_element_by_class_name('s_search')
	button.click()
	return browser.current_url # 返回关键字对应的网页
	browser.close()

def get_photo(new_url):
	"""
	为了进行图片url查找并下载
	new_url : 关键字对应的网页
	rerurn : 每个图片的具体网页
	"""
	# 这里要注意，爬取的地址中的图片可能需要下拉后才会加载到源码中，就需要自动下拉刷新图片
	browser = webdriver.Chrome(executable_path =  'E:\\chromedriver_win32\\chromedriver.exe')
	browser.get(new_url)

	# 设置加载超时时间
	wait = WebDriverWait(browser,10)
	i = 1
	while True:
		# 直到网页中的图片最后一个div加载成功。(每次加载新数据都是则将一个imgpaged的div)
		wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@id="imgid"]/div[last()]')))
		regx='http://[\S]*jpg'
		all_urls = re.findall(regx, browser.page_source)
		for url in all_urls:
			i = download_photo(url,i)
		# 将页面滚动底，加载新数据(执行js)
		browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
		# 页面加载需要时间
		#time.sleep(4+ random.random()*1)
		time.sleep(4)
	browser.close()

def download_photo(url,ji_shu):
	"""
	下载图片
	url : 具体图片地址
	"""
	r = requests.get(url)
	try:
		with open(r'E:\Photo\%s.jpg' % ji_shu,'wb') as f:
			print('开始下载图片,地址为{0}'.format(url))
			f.write(r.content)
			print('第{n}张图片已下载完毕\n'.format(n = ji_shu))
			return ji_shu + 1
	except:
		print('出现错误\n')
		return ji_shu

def main():
	n = input('请输入搜索内容:')
	print('您搜索的是{0}\n'.format(n))
	url = 'http://image.baidu.com/'
	my_url = get_url(url,n)
	get_photo(my_url)


if __name__ == '__main__':
	main()