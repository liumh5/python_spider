# -*- coding: utf-8 -*-
import json
import os
import random

from selenium import webdriver
import requests
from lxml import etree

if __name__ == '__main__' :
    proxies = ["222.85.28.130:52590", "117.191.11.80:80", "117.127.16.205:8080", "118.24.128.46:1080",
               "120.78.225.5:3128", "113.124.92.200:9999", "183.185.1.47:9797", "115.29.3.37:80", "36.248.129.158:9999",
               "222.89.32.182:9999", "117.191.11.111:80", "182.35.84.182:9999", "47.100.103.71:80",
               "121.63.209.92:9999", "124.193.37.5:8888", "39.135.24.11:8080", "14.146.95.4:9797", "182.35.83.244:9999",
               "113.120.36.179:9999", "1.199.31.90:9999", "58.17.125.215:53281", "212.64.51.13:8888",
               "182.35.84.135:9999", "163.204.247.60:9999", "39.106.35.21:3128", "202.39.222.32:80",
               "120.83.111.42:9999", "63.220.1.43:80", "42.238.85.70:9999", "117.191.11.107:80"]
    #    'Cookie': 'UOR=,weibo.com,english.koolearn.com; SINAGLOBAL=4091574218037.2227.1523757969828; SUB=_2A25wQBu8DeRhGedM4lUS8ybLyz2IHXVTNAp0rDV8PUNbmtBeLUjakW9NW4kNsV4Xq3hTbJbBfspnaCuIdj-Uusv-; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWIo6JPyWv32quobckfkRBJ5JpX5KzhUgL.Fo2E1KM0e0nNeh22dJLoIXnLxKBLBonL1h5LxKBLBonLB-2LxKBLB.2LB.2LxKML1-2L1hBLxKBLBonLBKBLxK-LBKBLBK.LxKBLBonL1h5LxK-LBKBL1-et; login_sid_t=1bcef5cce0db538ecdb6b2cbc2b9e7e1; cross_origin_proto=SSL; _s_tentry=-; Apache=4265585913858.3364.1564765093772; ULV=1564765093775:1:1:1:4265585913858.3364.1564765093772:; SUHB=0ElrLpu7ShJKOt; ALF=1596301164; SSOLoginState=1564765165; wvr=6; webim_unReadCount=%7B%22time%22%3A1564765870168%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A27%2C%22msgbox%22%3A0%7D'
    # 'Cookie': 'UOR=,weibo.com,login.sina.com.cn; SINAGLOBAL=4091574218037.2227.1523757969828; SUB=_2A25wQeJiDeRhGedM4lUS8ybLyz2IHXVTN1SqrDV8PUNbmtBeLUvBkW9NW4kNsTrCi_Jruy5MTxw54gPstTU-9tN1; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWIo6JPyWv32quobckfkRBJ5JpX5KzhUgL.Fo2E1KM0e0nNeh22dJLoIXnLxKBLBonL1h5LxKBLBonLB-2LxKBLB.2LB.2LxKML1-2L1hBLxKBLBonLBKBLxK-LBKBLBK.LxKBLBonL1h5LxK-LBKBL1-et; login_sid_t=1bcef5cce0db538ecdb6b2cbc2b9e7e1; cross_origin_proto=SSL; Ugrow-G0=5c7144e56a57a456abed1d1511ad79e8; YF-V5-G0=d30fd7265234f674761ebc75febc3a9f; _s_tentry=-; Apache=4265585913858.3364.1564765093772; ULV=1564765093775:1:1:1:4265585913858.3364.1564765093772:; wb_view_log=1536*8641.25; SUHB=0ftYuJD86bTuZ9; YF-Page-G0=237c624133c0bee3e8a0a5d9466b74eb|1564840792|1564840789; wb_view_log_1297338701=1536*8641.25; webim_unReadCount=%7B%22time%22%3A1564840916474%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A32%2C%22msgbox%22%3A0%7D; secsys_id=78a4800a0e324aab4c7cc0e3f6491d12; ALF=1596376497; SSOLoginState=1564840498'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
        'Cookie' : ''
    }

    # 当前路径+pic
    pic_file_path = os.path.join(os.path.abspath(''), 'pic')
    txt_file_path = os.path.join(os.path.abspath(''), 'txt')
    # params = {
    #     'ajwvr': 6,
    #     'id': '4387470198281748',
    #     'from': 'singleWeiBo',
    #     'root_comment_max_id': ''
    # }

    # URL = 'https://m.weibo.cn/api/comments/show?id=4400594393104944&page=1'
    # URL= 'https://m.weibo.cn/api/comments/show?id=4402666178106467&page=1'
    URL = 'https://www.google.com'
    # resp = requests.get(URL,  headers=headers, proxies={"http": random.choices(proxies)[0]})
    # resp = requests.get(URL,headers = headers,proxies={"http":"127.0.0.1:1080"})
    resp = requests.get(URL,headers = headers)

    # resp = json.loads(resp.text)
    print(resp.text)
    # html = resp['data']['html']
    # print(html)
    # html = etree.HTML(html)
    # if resp['code'] == '100000':
    #     print(resp)
    #     html = resp['data']['html']
    #     print(html)
    #     html = etree.HTML(html)