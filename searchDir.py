import os
import sys


path = sys.argv[1]
word = sys.argv[2]

ls =[]

for root,dirs,files in os.walk(path):
	for dir in dirs:
		if  dir == word:
			ls.append(os.path.join(root,dir))

for i in ls:
	print(i)
