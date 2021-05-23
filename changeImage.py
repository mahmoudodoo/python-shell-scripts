
#!/usr/bin/env python3

# images path : /home/student-03-83b686b86d95/supplier-data/images

from PIL import Image
import os

user = os.getenv('USER')
images_path = '/home/{}/supplier-data/images'.format(user)


for subdir,dirs,files in os.walk(images_path):
        for file in files:
                if file == 'LICENSE' or file == 'README':
                        continue
                else:
                        print(file)
                        im = Image.open(subdir+"/"+file)
                        rgb_im = im.convert('RGB')
                        os.remove(subdir+"/"+file)
                        rgb_im.resize((600,400)).save(subdir+"/"+file,"jpeg")
                        os.rename(subdir+"/"+file,subdir+"/"+file[:-4]+"jpeg")


