# -*- coding: utf-8 -*-

import json
import os
import random
import time
from urllib.parse import parse_qs

import requests
from lxml import etree

from GetCookie import GetCookie

"""
爬取微博评论
"""
# 代理设置
proxies = ["222.85.28.130:52590","117.191.11.80:80","117.127.16.205:8080","118.24.128.46:1080","120.78.225.5:3128","113.124.92.200:9999","183.185.1.47:9797","115.29.3.37:80","36.248.129.158:9999","222.89.32.182:9999","117.191.11.111:80","182.35.84.182:9999","47.100.103.71:80","121.63.209.92:9999","124.193.37.5:8888","39.135.24.11:8080","14.146.95.4:9797","182.35.83.244:9999","113.120.36.179:9999","1.199.31.90:9999","58.17.125.215:53281","212.64.51.13:8888","182.35.84.135:9999","163.204.247.60:9999","39.106.35.21:3128","202.39.222.32:80","120.83.111.42:9999","63.220.1.43:80","42.238.85.70:9999","117.191.11.107:80"]
#    'Cookie': 'UOR=,weibo.com,english.koolearn.com; SINAGLOBAL=4091574218037.2227.1523757969828; SUB=_2A25wQBu8DeRhGedM4lUS8ybLyz2IHXVTNAp0rDV8PUNbmtBeLUjakW9NW4kNsV4Xq3hTbJbBfspnaCuIdj-Uusv-; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWIo6JPyWv32quobckfkRBJ5JpX5KzhUgL.Fo2E1KM0e0nNeh22dJLoIXnLxKBLBonL1h5LxKBLBonLB-2LxKBLB.2LB.2LxKML1-2L1hBLxKBLBonLBKBLxK-LBKBLBK.LxKBLBonL1h5LxK-LBKBL1-et; login_sid_t=1bcef5cce0db538ecdb6b2cbc2b9e7e1; cross_origin_proto=SSL; _s_tentry=-; Apache=4265585913858.3364.1564765093772; ULV=1564765093775:1:1:1:4265585913858.3364.1564765093772:; SUHB=0ElrLpu7ShJKOt; ALF=1596301164; SSOLoginState=1564765165; wvr=6; webim_unReadCount=%7B%22time%22%3A1564765870168%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A27%2C%22msgbox%22%3A0%7D'
# headers文件设置
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
     'Cookie': ''
}


# 当前路径+pic
pic_file_path = os.path.join(os.path.abspath(''), 'pic')
txt_file_path = os.path.join(os.path.abspath(''), 'txt')

# 下载图片
def download_pic(url, nick_name):
    if not url:
        return
    if not os.path.exists(pic_file_path):
        os.mkdir(pic_file_path)
    # else:
    #     print(pic_file_path)
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(pic_file_path + f'/{nick_name}.jpg', 'wb') as f:
            f.write(resp.content)

# 写入文件
def write_file(file,string):
    if not os.path.exists(txt_file_path):
        os.mkdir(txt_file_path)
    # else:
    #     print(txt_file_path)
    with open(txt_file_path + f'/{file}.txt', 'a', encoding='utf-8') as f:
        f.write(string+'\n')
# 写入留言内容

# 获取子评论所需参数
comment_params = {
    'ajwvr': 6,
    'more_comment': 'big',
    'is_child_comment': 'true',
    'id': '4367970740108457',
    'from': 'singleWeiBo',
    'last_child_comment_id': '',
    'root_comment_id': '',
    'root_comment_max_id': ''
}


if __name__ == '__main__':
    params = {
        'ajwvr': 6,
        'id': '4402385319767344',
        'from': 'singleWeiBo',
        'root_comment_max_id': ''
    }
    params2 = {
        'ajwvr': 6,
        'id': '4402385319767344',
        'from': 'singleWeiBo',
        'root_comment_max_id': '',
        'page': ''
    }
    url = 'https://weibo.com/'
    # 获得浏览游客cookie
    c = GetCookie(url,10)
    headers['Cookie'] = c.get_dict_cookie()
    URL = 'https://weibo.com/aj/v6/comment/big'
    maxtmp_id = ''
    page = ''

    j = 0
    max_id = ''
    # 爬去100页，需要代理，或者进行sleep 不然会超时。
    for num in range(501):
        print(f'=========   正在读取第 {num} 页 ====================')

        print(params)
        # 请求配置好的地址获取html
        resp = requests.get(URL, params=params, headers=headers, proxies={"http": random.choices(proxies)[0]})
        # print(resp.text)
        resp = json.loads(resp.text)
        # print(resp)
        # 判断maxtmp_id是否有值，确定是否要从上次断开页面重新开始读取
        if maxtmp_id != '' :
            params2['root_comment_max_id'] = maxtmp_id
            params2['page'] = page
            params = params2
            maxtmp_id = ''
            continue

        if resp['code'] == '100000':
            # json中获取html
            html = resp['data']['html']
            # print(html)
            # etree规范html格式
            html = etree.HTML(html)

            # 获取下一节点相关root_comment_max_id和page
            try:
               node_params = parse_qs(html.xpath('//div[@node-type="comment_loading"]/@action-data')[0])
               print(node_params)
            except:
               print('expcept')
               node_params = parse_qs(html.xpath('//div[@node-type="comment_list"]/a/@action-data')[0])
               print(node_params)
            max_id = node_params['root_comment_max_id'][0]
            # 反复爬虫应当会触发微博反爬虫机制，在无用界面循环，暂时未解决
            if  max_id == '4387522853385150' :
                time.sleep(60)
                max_id = ''
                continue
                # print(resp['data']['html'])
                # break
            #     设置下一页面的关键信息
            params2['root_comment_max_id'] = max_id
            params2['page'] = node_params['page'][0]
            params = params2
            print("next pages: " + max_id + " next " + str(num + 1))
            write_file('maxid', max_id)

            # 解析当前页面的评论和图片地址
            data = html.xpath('//div[@class="list_ul"]/div[@node-type="root_comment"]/div[@class="list_con"]')
            # print(len(data))
            data = html.xpath('//div[@node-type="root_comment"]')
            # print(len(data))
            for i in data:
                nick_name = i.xpath('.//div[@class="WB_text"]/a/text()')[0]
                # print(nick_name)
                test = i.xpath('.//div[@class="WB_text"]/text()')
                #                print(test)
                wb_text = i.xpath('.//div[@class="WB_text"][1]/text()')
                # print(wb_text)

                write_file('comment',nick_name + '!!' + wb_text[1])
                # print(string)
                comment_id = i.xpath('./@comment_id')[0]
                # print(comment_id)
                # 评论的图片地址
                pic_url = i.xpath('.//li[@class="WB_pic S_bg2 bigcursor"]/img/@src')
                # print(pic_url)
                pic_url = 'https:' + pic_url[0] if pic_url else ''
                # print(pic_url)
                # download_pic(pic_url, nick_name)
                if pic_url != '' :
                   write_file('url',pic_url+' '+nick_name)
            time.sleep(5)

