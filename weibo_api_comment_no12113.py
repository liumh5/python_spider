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
# proxies = ["222.85.28.130:52590","117.191.11.80:80","117.127.16.205:8080","118.24.128.46:1080","120.78.225.5:3128","113.124.92.200:9999","183.185.1.47:9797","115.29.3.37:80","36.248.129.158:9999","222.89.32.182:9999","117.191.11.111:80","182.35.84.182:9999","47.100.103.71:80","121.63.209.92:9999","124.193.37.5:8888","39.135.24.11:8080","14.146.95.4:9797","182.35.83.244:9999","113.120.36.179:9999","1.199.31.90:9999","58.17.125.215:53281","212.64.51.13:8888","182.35.84.135:9999","163.204.247.60:9999","39.106.35.21:3128","202.39.222.32:80","120.83.111.42:9999","63.220.1.43:80","42.238.85.70:9999","117.191.11.107:80"]
#    'Cookie': 'UOR=,weibo.com,english.koolearn.com; SINAGLOBAL=4091574218037.2227.1523757969828; SUB=_2A25wQBu8DeRhGedM4lUS8ybLyz2IHXVTNAp0rDV8PUNbmtBeLUjakW9NW4kNsV4Xq3hTbJbBfspnaCuIdj-Uusv-; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWIo6JPyWv32quobckfkRBJ5JpX5KzhUgL.Fo2E1KM0e0nNeh22dJLoIXnLxKBLBonL1h5LxKBLBonLB-2LxKBLB.2LB.2LxKML1-2L1hBLxKBLBonLBKBLxK-LBKBLBK.LxKBLBonL1h5LxK-LBKBL1-et; login_sid_t=1bcef5cce0db538ecdb6b2cbc2b9e7e1; cross_origin_proto=SSL; _s_tentry=-; Apache=4265585913858.3364.1564765093772; ULV=1564765093775:1:1:1:4265585913858.3364.1564765093772:; SUHB=0ElrLpu7ShJKOt; ALF=1596301164; SSOLoginState=1564765165; wvr=6; webim_unReadCount=%7B%22time%22%3A1564765870168%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A27%2C%22msgbox%22%3A0%7D'
# headers文件设置
# cookie = '_T_WM=68855533210; WEIBOCN_FROM=1110006030; SUB=_2A25wSeziDeRhGeFM7FUX-SzIwzyIHXVTtfSqrDV6PUJbkdANLUb5kW1NQKYBCgO-TwnhC7m59WlPSXFEeK6NJQoM; SUHB=08J7tnUNhpiTJ1; MLOGIN=1;  M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076036718210039 ;XSRF-TOKEN='
# cookie= '_T_WM=68855533210; WEIBOCN_FROM=1110006030; SUB=_2A25wSeziDeRhGeFM7FUX-SzIwzyIHXVTtfSqrDV6PUJbkdANLUb5kW1NQKYBCgO-TwnhC7m59WlPSXFEeK6NJQoM; SUHB=08J7tnUNhpiTJ1; MLOGIN=1;  M_WEIBOCN_PARAMS=oid%3D4402385319767344%26luicode%3D20000061%26lfid%3D4402385319767344%26uicode%3D20000061%26fid%3D4402385319767344;XSRF-TOKEN='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
    # 'Cookie' : '_T_WM=68855533210;WEIBOCN_FROM=1110006030;SUB=_2A25wSeziDeRhGeFM7FUX-SzIwzyIHXVTtfSqrDV6PUJbkdANLUb5kW1NQKYBCgO-TwnhC7m59WlPSXFEeK6NJQoM;SUHB=08J7tnUNhpiTJ1;MLOGIN=1;XSRF-TOKEN=fa2fdf;M_WEIBOCN_PARAMS=uicode%3D20000174'
    'Cookie' : '_T_WM=68855533210; WEIBOCN_FROM=1110006030; SUB=_2A25wSeziDeRhGeFM7FUX-SzIwzyIHXVTtfSqrDV6PUJbkdANLUb5kW1NQKYBCgO-TwnhC7m59WlPSXFEeK6NJQoM; SUHB=08J7tnUNhpiTJ1; MLOGIN=1; XSRF-TOKEN=cac319'
}
headers2 = {
'Accept':'application/json, text/plain, */*',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'',
'Host':'m.weibo.cn',
'MWeibo-Pwa':'1',
'Referer':'https://m.weibo.cn/detail/4402385319767344',
'TE':'Trailers',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
'X-Requested-With':'XMLHttpRequest',
'X-XSRF-TOKEN':'74cca2'
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

def get_showid(comment_parameter):
    comment_url = []
    # user_id = {}
    # comment = {}
    # url = 'https://weibo.com/'
    # # 获得浏览游客cookie
    # c = GetCookie(url,10)
    # c.get_user_cookie()
    # headers['Cookie'] = c.get_dict_cookie()
    url = 'https://m.weibo.cn/api/comments/show?id='
    # 爬去100页，需要代理，或者进行sleep 不然会超时。

        # print(string)
    c_url_base = 'https://m.weibo.cn/api/comments/show?id='
    for parameter in comment_parameter:
        for page in range(101,1800):#提前知道每条微博只可抓取前100页评论
            dim_url = url + str(parameter) + "&page=" + str(page)
            comment_url.append(dim_url)

    #获取每个url下的user_id以及评论
    for dd_url in comment_url:
        print(dd_url)
        # u_c_r = requests.get(dd_url,headers=headers, proxies={"http": random.choices(proxies)[0]})
        u_c_r = requests.get(dd_url,headers = headers)
        print(json.loads(u_c_r.text))
        # print(u_c_r.text)
        for m in range(0,9):#提前知道每个url会包含9条用户信息
            resp = json.loads(u_c_r.text)
            one_comment = ""
            one_id = ""
            nick_name = ""
            pic_url = ""
            try:
                one_id = resp["data"]["data"][m]["user"]["id"]
                nick_name = resp["data"]["data"][m]["user"]["screen_name"]
            except:
                print("except1")
                # pass
            try:
                one_comment = resp["data"]["data"][m]["text"]
            except:
                print("except2")
                # pass
            try:
                pic_url = resp["data"]["data"][m]["pic"]["large"]["url"]
            except:
                print("except3")
                # pass

            # print(one_id)
            # print(nick_name)
            # print(one_comment)
            # print(pic_url)
            string1 = "nickname: " + nick_name + "!!one_id: " + str(one_id) + "!!text: " + one_comment + "!!pic_url: " + pic_url
            filename = "comment"
            write_file(filename,string1 )
            if pic_url != "" :
                filename = "url"
                write_file(filename,pic_url+' '+nick_name)
        time.sleep(5)

def get_hotflowid(comment_parameter,xsrf_token,cookie,maxidtmp,maxtypeidtmp):

   detailurl = "https://m.weibo.cn/detail/"
   config_url = "https://m.weibo.cn/api/config"
   hotflowurl = "https://m.weibo.cn/comments/hotflow?id=4402385319767344&mid=4402385319767344"
   maxtypeid_str = "&max_id_type="
   maxid_str = "&max_id="
   maxtypeid = ""
   maxid = ""
   # maxidtmp = "4402399365721403"
   # maxtypeidtmp = "1"
   for parameter in comment_parameter:
       hotflowurl = "https://m.weibo.cn/comments/hotflow?id="+str(parameter)+"&mid="+str(parameter)

       referurl = detailurl + parameter
       headers2.setdefault("Cookie",cookie+xsrf_token)
       headers2.setdefault("X-XSRF-TOKEN",xsrf_token)
       headers2.setdefault("Refer",referurl)
       config_resq = requests.get(config_url, headers=headers)
       config_json = json.loads(config_resq.text)
       print(config_json)
       xsrf_token = config_json["data"]["st"]
       headers2.setdefault("Cookie",cookie+xsrf_token)
       headers2.setdefault("X-XSRF-TOKEN",xsrf_token)
       if maxtypeidtmp == "":
           maxtypeid = maxtypeid_str + "0"
       else:
           maxid = maxid_str + maxidtmp
           maxtypeid = maxid + maxtypeid_str + maxtypeidtmp

       hotflowurl2 = hotflowurl + maxtypeid
       for i in range(0,2):
           config_resq = requests.get(config_url, headers=headers)
           config_json = json.loads(config_resq.text)
           xsrf_token = config_json["data"]["st"]
           headers2.setdefault("Cookie", cookie + xsrf_token)
           headers2.setdefault("X-XSRF-TOKEN", xsrf_token)
           for m in range(0, 3):
               hotflow_resq = requests.get(hotflowurl2, headers=headers)
               try:
                   hotflow_json = json.loads(hotflow_resq.text)
               except:
                   print(maxid)
                   print(maxtypeid)
                   print(hotflow_resq.text)
                   return
               print(hotflow_json)
               try:
                   maxid = maxid_str + str(hotflow_json["data"]["max_id"])
                   maxtypeid = maxtypeid_str + str(hotflow_json["data"]["max_id_type"])
               except:
                   print(hotflow_json)
                   print(hotflowurl2)
                   return
               hotflowurl2 = hotflowurl + maxid + maxtypeid
               for m in range(0, 19):  # 提前知道每个url会包含9条用户信息
                   one_comment = ""
                   one_id = ""
                   nick_name = ""
                   pic_url = ""
                   try:
                       one_id = hotflow_json["data"]["data"][m]["user"]["id"]
                       nick_name = hotflow_json["data"]["data"][m]["user"]["screen_name"]
                   except:
                       print("except1")
                       print("i:"+str(i))
                       print("m:" + str(m))
                       print(hotflowurl2)
                   # pass
                   try:
                       one_comment = hotflow_json["data"]["data"][m]["text"]
                   except:
                       print("except2")
                       print("i:" + str(i))
                       print("m:" + str(m))
                       print(hotflowurl2)
                   # pass
                   try:
                       pic_url = hotflow_json["data"]["data"][m]["pic"]["large"]["url"]
                   except:
                       print("except3")
                       print("i:"+str(i))
                       print("m:" + str(m))
                       print(hotflowurl2)
                   # pass

                   # print(one_id)
                   # print(nick_name)
                   # print(one_comment)
                   # print(pic_url)
                   string1 = "nickname: " + nick_name + "!!one_id: " + str(
                       one_id) + "!!text: " + one_comment + "!!pic_url: " + pic_url
                   filename = "comment"
                   write_file(filename, string1)
                   if pic_url != "":
                       filename = "url"
                       write_file(filename, pic_url + ' ' + nick_name)
           time.sleep(10)
       print(maxid)
       print(maxtypeid)
if __name__ == '__main__':
    cookie = 'MLOGIN=1; _T_WM=76071362675; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803%26uicode%3D20000174; SUB=_2A25wVQJ9DeRhGeFM7FUX-SzIwzyIHXVTua41rDV6PUJbkdAKLUvakW1NQKYBCiAGByIyI78P-Z7qn9zJ-ZAKISoi; SUHB=03oFX2dev1sGHa; XSRF-TOKEN='
    xsrf_token = "9f327f"

    # 网恋
    # comment_parameter = ['4402385680460377']
    # get_hotflowid(comment_parameter,"4402399365721403","1")
    # 比赛
    comment_parameter = ['4367970740108457']
    # get_showid(comment_parameter)
    # get_hotflowid(comment_parameter,xsrf_token,cookie,"","")
    get_hotflowid(comment_parameter,xsrf_token,cookie,"4368506122908768","1")