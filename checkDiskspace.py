#!/usr/bin/env python3
import os


def checkDiskSpace():
	return os.popen('df -h | grep -i sda').read()

print(checkDiskSpace())
