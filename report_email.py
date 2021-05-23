
#!/usr/bin/env python3

from reports import generate_report
import os
import datetime
import requests
from emails import generate_email,send_email
user = os.getenv('USER')

current_date = datetime.date.today().strftime('%B %d, %Y')
title = "Processed Update on" + str(current_date)



descriptions_path ='/home/{}/supplier-data/descriptions'.format(user)


info = ""
for subdir,dirs,files in os.walk(descriptions_path):
        for file in files:
                with open(descriptions_path+"/"+file) as f:
                        lines = f.readlines()
                        info += "name: " + lines[0]+ '<br />' +"weight: "+ lines[1] + '<br />' + '<br />'
#for data in response.json():
 #       print(data['name'])
  #      info += data['name'] + '<br />' + str(data['weight'])+' lbs' + '<br />' +'<br />'

generate_report('/tmp/processed.pdf',title,info)

email_subject = "Upload Completed - Online Fruit Store"
email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
msg = generate_email('automation@example.com','{}@example.com'.format(user), email_subject,email_body,'/tmp/processed.pdf')

send_email(msg)


