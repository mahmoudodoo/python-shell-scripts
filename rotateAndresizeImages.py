#!/usr/bin/env python3

from PIL import Image
import os

#/home/student-04-c55752c16d31/images

for subdir,dirs,files in os.walk('/home/student-04-c55752c16d31/images'):
        for file in files:
                if file == '.DS_Store':
                        continue
                else:
                        print(file)
                        im = Image.open(subdir+"/"+file)
                        rgb_im = im.convert('RGB')
                        rgb_im.rotate(90).resize((128,128)).save("/opt/icons/"+file,'jpeg')

