#!/usr/bin/env python3



import requests
import os
user = os.getenv('USER')
images_path = '/home/{}/supplier-data/images'.format(user)
url = "http://localhost/upload/"

for subdir,dirs,files in os.walk(images_path):
        for file in files:
                if file == 'LICENSE' or file == 'README':
                        continue
                else:        
                        with open(subdir+'/'+file, 'rb') as opened:
                            r = requests.post(url, files={'file': opened})

##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
