# Python 3.5
# Code I used to download the Pytorch Notebooks (there are 2 .rst files)

import os
import urllib.request as req
import shutil

def read_file():
    # this text file should be stored in the same directory as this script
    with open("all_tutorial_links.txt") as f:
        f_list = list(filter(lambda x:x!='',[line.strip() for line in f]))
    return f_list

def replace_hash(str1):
    if str1.startswith('# '):
        return str1.replace('# ','')
    elif str1.startswith('## '):
        return str1.replace('## ','')
    elif str1.startswith('### '):
        return str1.replace('### ','')
    else:
        return str1
    
def download_file(file_path):
    with req.urlopen(file_path) as response, open(os.path.basename(file_path),'wb') as out_file:
        shutil.copyfileobj(response, out_file)
        
def fix_name(str1):
    if ':' in str1:
        str1 = str1.replace(':','')
    return str1

def download_all(f_list, i_dict):
    # function is a bit messy, sorry
    # might rewrite later
    for key in i_dict:
        i1 = i_dict[key]
        dear0 = fix_name(f_list[key])
        os.mkdir(dear0)
        os.chdir(dear0)
        if isinstance(i1, dict):
            for key2 in i1:
                i2 = i1[key2]
                dear1 = fix_name(f_list[key2])
                os.mkdir(dear1)
                os.chdir(dear1)
                if isinstance(i2, dict):
                    for key3 in i2:
                        i3 = i2[key3]
                        dear2 = fix_name(f_list[key3])
                        os.mkdir(dear2)
                        os.chdir(dear2)
                        [download_file(f_list[item]) for item in i3]
                        os.chdir("../")
                elif isinstance(i2, list):
                    [download_file(f_list[item]) for item in i2]
                os.chdir("../")
        elif isinstance(i1, list):
            [download_file(f_list[item]) for item in i1]
        os.chdir("../")

# make sure you're in same directory as this script 
os.chdir(os.path.dirname(os.path.realpath(__file__)))
f = read_file()
f2 = list(map(lambda x:replace_hash(x), f))
ind_dict = {0:{1:list(range(2, 7)), 7:list(range(8, 12)), 12:{13:list(range(14, 16)), 16:list(range(17, 20)),
               20:list(range(21, 25))}, 25:[26], 27:[28], 29:list(range(30, 35))}, 35:list(range(36, 42)), 42:list(range(43, 47))}
os.mkdir('tutorial_nbs')        
os.chdir('tutorial_nbs')
download_all(f2, ind_dict)