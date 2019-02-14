# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:42:08 2019

@author: jdonovc
"""

# Python 3.5
# Download just the .ipynb files

import os
import urllib.request as req
import shutil
os.chdir('C:\\MyWorkingFolder\\PyTorch Tutorials New')

tutorial_links = []
with open('torch tutorials.txt') as f:
    for line in f:
        line = line.strip()
        if '.ipynb' in line:
            tutorial_links.append(line)
            
    
for file_path in tutorial_links:
    with req.urlopen(file_path) as response, open('notebooks\\'+os.path.basename(file_path),'wb') as out_file:
        shutil.copyfileobj(response, out_file)