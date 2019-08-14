# -*- coding: utf-8 -*-
import time

from Scripts.py3.Lib import os

def write_file(file,string):
    if not os.path.exists(txt_file_path):
        os.mkdir(txt_file_path)
    # else:
    #     print(txt_file_path)
    with open(txt_file_path + f'/{file}.txt', 'a', encoding='utf-8') as f:
        f.write(string+'\n')

def main(source_file):
    if not os.path.exists(txt_file_path):
        return
    # else:
    #     print(txt_file_path)
    in_text = open(txt_file_path + f'/{source_file}.txt', 'r', encoding='utf-8')

    for line in in_text.readlines():
        string = line.split(' ', -1)
        old_file = os.path.join(pic_file_path , string[0])
        new_file = os.path.join(pic_file_path , string[1].rstrip("\n") + ".jpg" )
        # print(old_file)
        # print(new_file)
        if os.path.exists(old_file) :
           if os.path.exists(new_file):
               t = time.time()
               new_file = os.path.join(pic_file_path, string[1].rstrip("\n") + "_"+str(round(t * 1000))+".jpg")
               time.sleep(1)
           os.rename(old_file, new_file)



if __name__ == "__main__" :
    txt_file_path = os.path.join(os.path.abspath(''), 'txt')
    pic_file_path = os.path.join(os.path.abspath(''), 'pic')

    source_file = "sp_file"
    main(source_file)