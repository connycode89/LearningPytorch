# Python 3.5
# Code I used to download the Pytorch Notebooks (there are 2 .rst files)

import os
import urllib.request as req
import shutil

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.mkdir('tutorial_nbs')

def read_file():
    with open("all_tutorial_links.txt") as f:
        f_list = list(filter(lambda x:x!='',[line.strip() for line in f]))
    return f_list

def hash_index(file_conts):
    l1 = len(file_conts)
    hash1 = [num for num in range(len(file_conts)) if file_conts[num].startswith('# ')]+[l1]
    hash2 = [num for num in range(len(file_conts)) if file_conts[num].startswith('## ')]+[l1]
    hash3 = [num for num in range(len(file_conts)) if file_conts[num].startswith('### ')]+[l1]
    inds4 = [num for num in range(len(file_conts)) if not file_conts[num].startswith('#')]
    return hash1, hash2, hash3, inds4

def create_dict1(h):
    for num2 in range(len(h)-1):
        list_a, list_b = h[num2], h[num2+1]
        for num in range(len(list_a)-1):
            d1, d2 = list_a[num], list_a[num+1]
            print([item for item in list_b if item>d1 and item<d2])
            
        
    
    dict1 = {}
        
    
def download_file(file_path):
    with req.urlopen(file_path) as response, open(os.path.basename(file_path),'wb') as out_file:
        shutil.copyfileobj(response, out_file)
        
f = read_file()
h = hash_index(f)
d1 = create_dict1(h)
#download_file('http://pytorch.org/tutorials/_downloads/tensor_tutorial.ipynb')