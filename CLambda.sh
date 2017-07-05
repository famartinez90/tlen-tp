#!/usr/bin/env python
import sys
from analyzer import parse

line = raw_input()
while  line :	
	try:		
		print line
		print parse(line)
		print "-------------"
		line = raw_input()
	except:
		line = ""

