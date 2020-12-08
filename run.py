  GNU nano 3.2                                      /home/student-01-264ae638e499/run.py                                                

#!/usr/bin/env python3

import os
import requests

user = os.getenv('USER')
url = "http://localhost/fruits/"
descriptions_path ='/home/{}/supplier-data/descriptions'.format(user)
images_lists = os.listdir('/home/{}/supplier-data/images'.format(user))
images_lists.remove('LICENSE')
images_lists.remove('README')
i=0
for subdir,dirs,files in os.walk(descriptions_path):
        for file in files:
                with open(descriptions_path+"/"+file) as f:
                        lines = f.readlines()
                        data={'name':lines[0].replace('\n','') , 'weight': int( lines[1].replace('\n','').replace(' lbs','') ) ,'descri$
                        'image_name':images_lists[i] }
                        r = requests.post(url,json=data)
                        i +=1

