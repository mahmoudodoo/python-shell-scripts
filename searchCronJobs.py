#!/usr/bin/env python3

import sys
import os


#initialize variables
from_node = sys.argv[1] # Searching for word in all cronjobs will start from this node (First Node)
to_node = sys.argv[2] # Stopping searching (The Last Node That we will search in)
host = '127.0.1.' # Host Number to the entier cluster
word = sys.argv[3] # this is the word that we want to find 

# Adding condition to check if nodes between 1 and 70
if not(from_node > 0 and to_node <= 70):
	print("Somthing wrong !! Please Enter node numbers correctly between 1 and 70 !!!")
	sys.exit()

# Visiting all nodes node by node to find any cronjob that contains our word
for node in range(from_node,to_node):
	os.system('ssh {}{} \"crontab -l | grep -i {}\" >> outPut.txt'.format(host,node,word))


# This comment from cronJobSearching Branch

