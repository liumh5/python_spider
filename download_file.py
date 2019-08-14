# -*- coding: utf-8 -*-
import os
import time
import urllib
import random
import requests

proxies = ["222.85.28.130:52590", "117.191.11.80:80", "117.127.16.205:8080", "118.24.128.46:1080", "120.78.225.5:3128",
           "113.124.92.200:9999", "183.185.1.47:9797", "115.29.3.37:80", "36.248.129.158:9999", "222.89.32.182:9999",
           "117.191.11.111:80", "182.35.84.182:9999", "47.100.103.71:80", "121.63.209.92:9999", "124.193.37.5:8888",
           "39.135.24.11:8080", "14.146.95.4:9797", "182.35.83.244:9999", "113.120.36.179:9999", "1.199.31.90:9999",
           "58.17.125.215:53281", "212.64.51.13:8888", "182.35.84.135:9999", "163.204.247.60:9999", "39.106.35.21:3128",
           "202.39.222.32:80", "120.83.111.42:9999", "63.220.1.43:80", "42.238.85.70:9999", "117.191.11.107:80"]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    # ,'Cookie': 'UOR=,weibo.com,login.sina.com.cn; SINAGLOBAL=4091574218037.2227.1523757969828; SUB=_2AkMqGY02dcPxrAJTkf8Wz2PlbIxH-jyZzOTAAn7uJhMyAxgv7mYAqSVutBF-XIQFZeRL5NrThCTP33zwmAIEtnUe; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WWIo6JPyWv32quobckfkRBJ5JpVFgyyd0eES0-peBtt; login_sid_t=1bcef5cce0db538ecdb6b2cbc2b9e7e1; cross_origin_proto=SSL; _s_tentry=-; Apache=4265585913858.3364.1564765093772; ULV=1564765093775:1:1:1:4265585913858.3364.1564765093772:; SUHB=0ElrLpu7ShJKOt; webim_unReadCount=%7B%22time%22%3A1564803580003%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A29%2C%22msgbox%22%3A0%7D; secsys_id=78a4800a0e324aab4c7cc0e3f6491d12; WBStorage=edfd723f2928ec64|undefined'
}


# 下载图片
def download_pic(url, pic_file_path, nick_name):
    if not url:
        return
    if not os.path.exists(pic_file_path):
        os.mkdir(pic_file_path)
    # else:
    #     print(pic_file_path)
    # urllib.request.urlretrieve(url, pic_file_path + f'/{nick_name}.jpg')
    # print(pic_file_path + f'\{nick_name}.jpg' + '.jpg保存成功。')
    resp = requests.get(url, headers=headers, proxies={"http": random.choices(proxies)[0]})
    if resp.status_code == 200:
        # print('pic_file_path 图片下载。。。')
        with open(pic_file_path + f'/{nick_name}.jpg', 'wb') as f:
            f.write(resp.content)
            f.close()
            print(nick_name + '.jpg保存成功。')
    time.sleep(2)


def read_file(filename):
    # 当前路径+pic
    pic_file_path = os.path.join(os.path.abspath(''), 'pic')
    txt_file_path = os.path.join(os.path.abspath(''), 'txt')

    if not os.path.exists(txt_file_path):
        return
    # else:
    #     print(txt_file_path)
    in_text = open(txt_file_path + f'/{filename}.txt', 'r', encoding='utf-8')
    i = 0
    j = 2
    for line in in_text.readlines():
        string = line.split(' ', -1)
        # print(str[0])
        # print(str[1].replace('\n',''))

        i = i + 1
        # if i == 200:
        #     time.sleep(60)
        #     i = 0
        #     pic_file_path = os.path.join(os.path.abspath(''), 'pic' + str(j))
        #     j = j + 1

        download_pic(string[0], pic_file_path, string[1].replace('\n', ''))
        # download_pic(string[0], pic_file_path, '图片'+str(i))


if __name__ == '__main__':
    read_file('url19081011')
    read_file('url19081012')
    read_file('url19081013')
    read_file('url19081014')
    read_file('url19081015')
