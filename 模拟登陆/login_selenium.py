#-*-coding:utf-8-*- 
# @File    : login_selenium.py

from selenium import webdriver
import selenium
# 1.�selenium+webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False
driver = webdriver.Chrome(chrome_options=chrome_options)
# 2.���û�����Ϣ
login_url = 'https://accounts.douban.com/passport/login'

headers = {

}

data = {

}

username = '18610059580'
password = '******'

# 3.ģ���½
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
# 	#���������֤�룬���浱ǰҳ�棬�鿴��ͼ��������֤�룬����֤��
# 	driver.save_screenshot("��ͼ�鿴��֤��.png")
# 	# ������֤��
# 	check_code = input("��������֤��:")#ʹ�ô���ƽ̨ʶ��ͼƬ
# 	print(r"��֤���Ƕ���:%s" % check_code)
#
# 	captcha_field = driver.find_element_by_id("captcha_field")
# 	#������֤������
# 	captcha_field.send_keys(check_code)
#
#
# except Exception as e:
# 	print("������")


driver.save_screenshot('��½�����.jpg')

# 4.��β
driver.close()


"""
1.��Ҫ���Ե���ҳ����ȡ��¼ǰ��cookie������ץ����ȡ�����Դ���ʵ�֣�����ḽ�ϴ��룩��

2.�ֶ���¼���ٻ�ȡ��¼���cookie��

3.�Ա����λ�ȡ��cookie���ҳ���¼��������cookie��ֻҪ�������name��value���У�һ��name����token����

4.�ڴ��������д��cookie�����ҳ�����name��valueд�롣Ȼ����дһ�����ҳ�Ĵ��롣

������ϴ��루��Ҫ�ż����ƴ���Ϊ�Լ����ã���������д���ƣ���Щ��¼�������Ҳ������ȥ����������

#coding=utf-8
from selenium import webdriver
import time
#����������ôд��ȥ���ȸ������������ʾ�ģ��ڶ��к͵����зֱ��Ӧ��ͬ����ʾ
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
# options.add_argument('disable-infobars')
browser = webdriver.Chrome(chrome_options=options)
#
browser.maximize_window()
#�򿪻�������
# browser=webdriver.Firefox()
#������ַ
browser.get("https://m.flycua.com/h5/#/")
#�����¼��������ע�͵Ĵ����ȡcookie��ʵ��������¼��ִ�нű���ʱ��Ͳ����ⲿ����
# browser.find_element_by_id("su").click()
# cookie1= browser.get_cookies()
#��ӡ��¼ǰ��cookie
# print (cookie1)
#�ȴ�30�룬����30��ʱ����ɵ�¼����
# time.sleep(30)
#��ȡ��¼���cookie
# cookie2= browser.get_cookies()
#��ӡ��¼���cookie
# print (cookie2)
#
#����Ҫ��ȡ��cookie��д��ȥ
browser.add_cookie({'name':'tokenId', 'value':'8BB8FDD4FBB31F92424A7E0EBE872E01A4AF77654043DAD638E9F93B378F94E19A882A6C7E78999C9A5482985FDA333C3D1E5236C6BDA7935A89178F053FB490'})
#�ٴ�������ַ
browser.get("https://m.flycua.com")
"""