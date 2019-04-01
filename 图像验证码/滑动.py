#-*-coding:utf-8-*- 
# @File    : ����.py
import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = '18610059580'
PASSWORD = '659190'
BORDER = 6
INIT_LEFT = 60


class CrackGeetest():
    def __init__(self):
        self.url = 'https://account.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD

    def __del__(self):
        self.browser.close()

    def get_geetest_button(self):
        """
        ��ȡ��ʼ��֤��ť
        :return:
        """
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        return button

    def get_position(self):
        """
        ��ȡ��֤��λ��
        :return: ��֤��λ��Ԫ��
        """
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)

    def get_screenshot(self):
        """
        ��ȡ��ҳ��ͼ
        :return: ��ͼ����
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_slider(self):
        """
        ��ȡ����
        :return: �������
        """
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    def get_geetest_image(self, name='captcha.png'):
        """
        ��ȡ��֤��ͼƬ
        :return: ͼƬ����
        """
        top, bottom, left, right = self.get_position()
        print('��֤��λ��', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    def open(self):
        """
        ����ҳ�����û�������
        :return: None
        """
        self.browser.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.ID, 'email')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        email.send_keys(self.email)
        password.send_keys(self.password)

    def get_gap(self, image1, image2):
        """
        ��ȡȱ��ƫ����
        :param image1: ����ȱ��ͼƬ
        :param image2: ��ȱ��ͼƬ
        :return:
        """
        left = 60
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i
                    return left
        return left

    def is_pixel_equal(self, image1, image2, x, y):
        """
        �ж����������Ƿ���ͬ
        :param image1: ͼƬ1
        :param image2: ͼƬ2
        :param x: λ��x
        :param y: λ��y
        :return: �����Ƿ���ͬ
        """
        # ȡ����ͼƬ�����ص�
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
                pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def get_track(self, distance):
        """
        ����ƫ������ȡ�ƶ��켣
        :param distance: ƫ����
        :return: �ƶ��켣
        """
        # �ƶ��켣
        track = []
        # ��ǰλ��
        current = 0
        # ������ֵ
        mid = distance * 4 / 5
        # ������
        t = 0.1
        # ���ٶ�
        v = 0

        while current < distance:
            if current < mid:
                # ���ٶ�Ϊ��2
                a = 2
            else:
                # ���ٶ�Ϊ��3
                a = -3
            # ���ٶ�v0
            v0 = v
            # ��ǰ�ٶ�v = v0 + at
            v = v0 + a * t
            # �ƶ�����x = v0t + 1/2 * a * t^2
            move = v0 * t + 1 / 2 * a * t * t
            # ��ǰλ��
            current += move
            # ����켣
            track.append(round(move))
        return track

    def move_to_gap(self, slider, track):
        """
        �϶����鵽ȱ�ڴ�
        :param slider: ����
        :param track: �켣
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in track:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()

    def login(self):
        """
        ��¼
        :return: None
        """
        submit = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-btn')))
        submit.click()
        time.sleep(10)
        print('��¼�ɹ�')

    def crack(self):
        # �����û�������
        self.open()
        # �����֤��ť
        button = self.get_geetest_button()
        button.click()
        # ��ȡ��֤��ͼƬ
        image1 = self.get_geetest_image('captcha1.png')
        # �㰴����ȱ��
        slider = self.get_slider()
        slider.click()
        # ��ȡ��ȱ�ڵ���֤��ͼƬ
        image2 = self.get_geetest_image('captcha2.png')
        # ��ȡȱ��λ��
        gap = self.get_gap(image1, image2)
        print('ȱ��λ��', gap)
        # ��ȥȱ��λ��
        gap -= BORDER
        # ��ȡ�ƶ��켣
        track = self.get_track(gap)
        print('�����켣', track)
        # �϶�����
        self.move_to_gap(slider, track)

        success = self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_success_radar_tip_content'), '��֤�ɹ�'))
        print(success)

        # ʧ�ܺ�����
        if not success:
            self.crack()
        else:
            self.login()


if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()