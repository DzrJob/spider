#-*-coding:utf-8-*- 
# @File    : ����ͼƬ������.py
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


import time




def get_snap(driver):
    """
    �õ����ն���
    :param driver:
    :return:
    """
    driver.save_screenshot('full_snap.png')     # ����ͼƬ
    page_snap_obj=Image.open('full_snap.png')   # ��ȡͼƬ
    return page_snap_obj                        # ����ͼƬ����

def get_image(driver):
    """

    :param driver:
    :return:
    """
    img=driver.find_element_by_class_name('geetest_canvas_img')
    time.sleep(2)
    # ��ȡͼƬ����
    location=img.location
    # ��ȡͼ��ߴ�
    size=img.size

    left=location['x']
    top=location['y']
    right=left+size['width']
    bottom=top+size['height']
    # {'x': 238, 'y': 15} {'height': 159, 'width': 258} 238 15 496 174
    # print(location,size,left,top,right,bottom)
    page_snap_obj=get_snap(driver)
    # print(np.array(page_snap_obj))
    # plt.imshow(page_snap_obj)
    # plt.show()
    image_obj=page_snap_obj.crop((left,top,right,bottom))
    image_obj.show()        # չʾͼƬ
    return image_obj

def get_distance(image1,image2):
    start=57
    threhold=60     # ��ֵ

    # print('image1',image1)
    # print('image1',image1.size[0])
    # print('image1',image1.size[1])
    """
    image1 <PIL.Image.Image image mode=RGBA size=258x159 at 0x1CB8E32EAC8>
    image1 258
    image1 159
    """
    """
    i,j 101 63
    (186, 190, 202, 255)
    (123, 126, 135, 255)
    63 186 123
    64 190 126
    """
    for i in range(start,image1.size[0]):
        for j in range(image1.size[1]):
            # print('i,j',i,j)
            rgb1=image1.load()[i,j]
            # print(rgb1)
            rgb2=image2.load()[i,j]
            # print(rgb2)
            res1=abs(rgb1[0]-rgb2[0])
            # print(res1,rgb1[0],rgb2[0])
            res2=abs(rgb1[1]-rgb2[1])
            # print(res2,rgb1[1],rgb2[1])
            res3=abs(rgb1[2]-rgb2[2])
            if not (res1 < threhold and res2 < threhold and res3 < threhold):
                return i-7
    return i-7

def get_tracks(distance):
    distance+=20 #�Ȼ���һ�㣬����ٷ��Ż�������
    v=0
    t=0.2
    forward_tracks=[]

    current=0
    mid=distance*3/5
    while current < distance:
        if current < mid:
            a=2
        else:
            a=-3

        s=v*t+0.5*a*(t**2)
        v=v+a*t
        current+=s
        forward_tracks.append(round(s))

    #���Ż�����׼ȷλ��
    back_tracks=[-3,-3,-2,-2,-2,-2,-2,-1,-1,-1] #�ܹ�����-20

    return {'forward_tracks':forward_tracks,'back_tracks':back_tracks}

def crack(driver): #�ƽ⻬����֤

    # 1�������ť���õ�û��ȱ�ڵ�ͼƬ
    button = driver.find_element_by_class_name('geetest_radar_tip')
    button.click()
    time.sleep(2)
    js = 'document.getElementsByClassName("geetest_canvas_fullbg geetest_fade geetest_absolute")[0].style="opacity: 1; display: block;"'
    js2 = "alert(document.getElementsByClassName('geetest_canvas_fullbg geetest_fade geetest_absolute'))"
    # ����js�ű�
    # driver.execute_script(js)
    driver.execute_script(js)

    # 2����ȡû��ȱ�ڵ�ͼƬ
    image1 = get_image(driver)

    # 3�����������ť���õ���ȱ�ڵ�ͼƬ
    button = driver.find_element_by_class_name('geetest_slider_button')
    button.click()

    # 4����ȡ��ȱ�ڵ�ͼƬ
    image2 = get_image(driver)

    # 5���Ա�����ͼƬ�����ص㣬�ҳ�λ��
    distance = get_distance(image1, image2)

    # 6��ģ���˵���Ϊϰ�ߣ�������λ�Ƶõ���Ϊ�켣
    tracks = get_tracks(distance)
    print(tracks)

    # 7�������ж��켣�����򻬶����󷴻���
    button = driver.find_element_by_class_name('geetest_slider_button')
    ActionChains(driver).click_and_hold(button).perform()

    # ���������������������ؿ�ʼ���򻬶������ŵر����Ƿ�����
    for track in tracks['forward_tracks']:
        ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()

    # ���ɵ���ˣ�����������ͣ����һ�£��ع��������֣��Բۣ�������,Ȼ��ʼ���򻬶�
    time.sleep(0.5)
    for back_track in tracks['back_tracks']:
        ActionChains(driver).move_by_offset(xoffset=back_track, yoffset=0).perform()

    # С��Χ��һ�£���һ���Ի����̨����һ�����Լ������߳ɹ���
    ActionChains(driver).move_by_offset(xoffset=-3, yoffset=0).perform()
    ActionChains(driver).move_by_offset(xoffset=3, yoffset=0).perform()

    # �ɹ���ɧ��������ϲ��ĬĬ������һ���Լ�ƴͼ�ĳɹ���Ȼ������������ɿ���ֻ����
    time.sleep(0.5)
    ActionChains(driver).release().perform()

def login_cnblogs(username,password):
    driver = webdriver.Chrome()
    try:
        # 1�������˺�����س�
        driver.implicitly_wait(3)
        driver.get('https://passport.cnblogs.com/user/signin')

        input_username = driver.find_element_by_id('input1')
        input_pwd = driver.find_element_by_id('input2')
        signin = driver.find_element_by_id('signin')

        input_username.send_keys(username)
        input_pwd.send_keys(password)
        signin.click()

        # 2���ƽ⻬����֤
        crack(driver)

        time.sleep(1000000)  # ˯ʱ�䳤һ�㣬ȷ����¼�ɹ�
    finally:
        # driver.close()
        pass

if __name__ == '__main__':
    login_cnblogs(username='Mr.dzr',password='djj1211#1')