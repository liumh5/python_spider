# -*- coding: utf-8 -*-
import json
import os
import urllib

from PIL import Image
from selenium import webdriver
from time import sleep

# 获取登录后的cookies
from selenium.webdriver.firefox.options import Options


class GetCookie:
    # 初始化浏览器和网址
    def __init__(self, url,stime,viewflag):
        self.url = url
        if viewflag == 1 :
            self.firefox_opt = Options()
            self.firefox_opt.add_argument("--headless")
            self.firefox_opt.add_argument("--disable-gpu")
            self.firefox_opt.add_argument("--window-size=1366,768")
            self.driver = webdriver.Firefox(firefox_options=self.firefox_opt)
        else:
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(stime)
        self.r = self.driver.get(self.url)

        # sleep(stime)
    # 通过用户密码登陆网址
    def login(self,name,passwd,stime):
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(name)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(passwd)
        self.driver.find_element_by_xpath("//input[@id='btnlogin']").click()
        sleep(stime)
    #  获取原始cookie数据
    def phone_login(self,phoneid,stime):
        print(self.driver.page_source)
        self.driver.find_element_by_class_name("input-container").send_keys(phoneid)
        self.driver.find_element_by_class_name("m-btn-blue-hover").click()
        print(self.driver.page_source)
        if self.driver.find_element_by_class_name("number-code"):
            print("输入收到的短信验证码")
            ycode = input()
            self.driver.find_element_by_class_name("number-code").send_keys(ycode)
            if self.driver.find_element_by_class_name("m-btn-blue") :
                self.driver.find_element_by_class_name("m-btn-blue").click()
        # sleep(stime)


    def get_headers(self):
        logs = [json.loads(log['message'])['message'] for log in self.driver.get_log('performance')]
        return logs;
    def get_cookie(self):
        cookie = self.driver.get_cookies()
        print(cookie)
        self.cookie = cookie
        return self.cookie
    # 获取字典数据格式的cookie
    def get_dict_cookie(self):
        # cookie = ';'.join(item for item in ["'" + item["name"] + "'" + "=" + "'" + item["value"] + "'" for item in self.driver.get_cookies()])
        cookie = ';'.join(item for item in [item["name"] + "="  + item["value"] for item in self.driver.get_cookies()])
        print(cookie)
        return cookie

    # 下载指定图片
    def get_picture(self,url,pic_name):
        pic_file_path = os.path.join(os.path.abspath(''), 'pic')

        if not url:
            return
        if not os.path.exists(pic_file_path):
            os.mkdir(pic_file_path)
        urllib.request.urlretrieve(url, pic_file_path + f'/{pic_name}.jpg')
    # 展示图片
    def show_picture(self,pic_name):
        pic_file_path = os.path.join(os.path.abspath(''), 'pic')
        if not os.path.exists(pic_file_path):
            return
        im = Image.open(pic_file_path + f'/{pic_name}.jpg')
        im.show()
    # 通过验证码登陆，下载并展示验证码图片
    def get_user_cookie(self):
        # 点击验证码选项出出发验证码图片生成
        self.driver.find_element_by_class_name("qrcode_target").click()
        self.driver.find_element_by_class_name("qrcode_target").click()
        pic_name = "target_pic"
        # 获取验证码图片地址并下载后展示
        if self.driver.find_element_by_class_name("login_content").find_element_by_tag_name("img") :
           url = self.driver.find_element_by_class_name("login_content").find_element_by_tag_name("img").get_attribute("src")
           self.get_picture(url,pic_name)
           self.show_picture(pic_name)
        # sleep(10)
if __name__ == '__main__':
    # url = 'https://weibo.com/'
    # c = GetCookie(url,20)
    # c.get_cookie()
    # c.get_user_cookie()
    # # c.get_cookie()
    # c.get_dict_cookie()
    url = "https://m.weibo.cn/login?backURL=https%253A%252F%252Fm.weibo.cn%252F"
    c = GetCookie(url, 20, 1)
    c.get_cookie()
    try:
        c.phone_login("18612416684",60)
        c.get_dict_cookie()
        c.driver.quit()
        # print(c.get_headers())
    except:
        c.driver.quit()