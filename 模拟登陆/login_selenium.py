#-*-coding:utf-8-*- 
# @File    : login_selenium.py

from selenium import webdriver
import selenium
# 1.搭建selenium+webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False
driver = webdriver.Chrome(chrome_options=chrome_options)
# 2.配置基础信息
login_url = 'https://accounts.douban.com/passport/login'

headers = {

}

data = {

}

username = '18610059580'
password = '******'

# 3.模拟登陆
driver.get(login_url)

login_use_account = driver.find_element_by_class_name('account-tab-account')
login_use_account.click()

input_username = driver.find_element_by_id('username')
input_password = driver.find_element_by_id('password')

input_username.send_keys(username)
input_password.send_keys(password)

login_btn = driver.find_element_by_xpath('//a[@class="btn btn-account btn-active"]')
login_btn.click()



# try:
# 	#如果出现验证码，保存当前页面，查看截图，输入验证码，到验证框
# 	driver.save_screenshot("截图查看验证码.png")
# 	# 输入验证码
# 	check_code = input("请输入验证码:")#使用打码平台识别图片
# 	print(r"验证码是多少:%s" % check_code)
#
# 	captcha_field = driver.find_element_by_id("captcha_field")
# 	#输入验证码内容
# 	captcha_field.send_keys(check_code)
#
#
# except Exception as e:
# 	print("报错了")


driver.save_screenshot('登陆后界面.jpg')

# 4.收尾
driver.close()


"""
1.打开要测试的网页，获取登录前的cookie（可以抓包获取，可以代码实现，下面会附上代码）。

2.手动登录，再获取登录后的cookie。

3.对比两次获取的cookie，找出登录后多出来的cookie，只要多出来的name和value就行（一般name就是token）。

4.在代码里加上写入cookie，把找出来的name和value写入。然后再写一遍打开网页的代码。

下面放上代码（不要着急复制代码为自己所用，代码后面会写限制，有些登录用这代码也跳不过去，哈哈）。

#coding=utf-8
from selenium import webdriver
import time
#下面四行这么写是去掉谷歌浏览器上面提示的，第二行和第三行分别对应不同的提示
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
# options.add_argument('disable-infobars')
browser = webdriver.Chrome(chrome_options=options)
#
browser.maximize_window()
#打开火狐浏览器
# browser=webdriver.Firefox()
#输入网址
browser.get("https://m.flycua.com/h5/#/")
#点击登录，用下面注释的代码获取cookie，实现跳过登录，执行脚本的时候就不用这部分了
# browser.find_element_by_id("su").click()
# cookie1= browser.get_cookies()
#打印登录前的cookie
# print (cookie1)
#等待30秒，用这30秒时间完成登录操作
# time.sleep(30)
#获取登录后的cookie
# cookie2= browser.get_cookies()
#打印登录后的cookie
# print (cookie2)
#
#加入要获取的cookie，写进去
browser.add_cookie({'name':'tokenId', 'value':'8BB8FDD4FBB31F92424A7E0EBE872E01A4AF77654043DAD638E9F93B378F94E19A882A6C7E78999C9A5482985FDA333C3D1E5236C6BDA7935A89178F053FB490'})
#再次输入网址
browser.get("https://m.flycua.com")
"""