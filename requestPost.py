#! /usr/bin/env python3

import os
import requests


# This script converts a bunch of .txt files to dictionaries and post them to website

listTxt = os.listdir('/data/feedback')
print(listTxt)

url = 'http://34.122.190.223/feedback/'

#response = requests.get('http://34.122.190.223')
for f in listTxt:
        with open('/data/feedback/'+f) as file:
                lines = file.readlines()
                data={
                                'title':lines[0].replace('\n',''),
                                'name':lines[1].replace('\n',''),
                                'date':lines[2].replace('\n',''),
                                'feedback':lines[3].replace('\n','')
                        }
        r = requests.post(url,data)


