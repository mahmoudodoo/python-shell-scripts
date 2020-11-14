import os
from os.path import join,getsize



for root, dirs, files in os.walk('/home/mahmoudodeh/Desktop/Ethical Hacking Python'):
    print(root, end=" ")
    print(sum([getsize(join(root,name)) for name in files]),end=" " )
    print('Bytes in', len(files), 'non-directory files')
