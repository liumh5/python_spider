# -*- coding: utf-8 -*-
from Scripts.py3.Lib import os

def write_file(file,string):
    if not os.path.exists(txt_file_path):
        os.mkdir(txt_file_path)
    # else:
    #     print(txt_file_path)
    with open(txt_file_path + f'/{file}.txt', 'a', encoding='utf-8') as f:
        f.write(string+'\n')

def main(source_file,dim_file):
    if not os.path.exists(txt_file_path):
        return
    # else:
    #     print(txt_file_path)
    in_text = open(txt_file_path + f'/{source_file}.txt', 'r', encoding='utf-8')

    for line in in_text.readlines():
        string = line.split(' ', -1)

        write_file(dim_file,string[0])



if __name__ == "__main__" :
    txt_file_path = os.path.join(os.path.abspath(''), 'txt')

    # source_file="url19081011"
    # dim_file="one_file"
    # main(source_file,dim_file)
    # source_file="url19081012"
    # dim_file="one_file"
    # main(source_file,dim_file)
    # source_file="url19081013"
    # dim_file="one_file"
    # main(source_file,dim_file)
    # source_file="url19081014"
    # dim_file="one_file"
    # main(source_file,dim_file)
    # source_file="url19081015"
    # dim_file="one_file"
    # main(source_file,dim_file)
    source_file = "url"
    dim_file = "one_file"
    main(source_file,dim_file)