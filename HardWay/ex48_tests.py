# https://blog.csdn.net/jnu_simba/article/details/12104371

#!/usr/bin/env python
#coding = utf-8

import re

def convert_number(s):
	try:
	    return int(s)
	except ValueError:
	    return None

def scan(input_str):
    
    words = input_str.split('')
    
    pattern = re.compile(r'\d+')
    
    direction_list = ['north', 'south', ]