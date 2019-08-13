#!/usr/local/bin/python3


#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               Email: faisalkhan91@outlook.com                             #
#                               Date: 8/13/2019                                              #
#############################################################################################

# Importing system module

import re
import sys
import os

if len(sys.argv) != 2:
	print("Error - must supply name of program to search")
else:
	if os.path.isfile(sys.argv[1]):
		programfile = open(sys.argv[1])
		programtext = programfile.read()
		programfile.close()

		name = re.compile(r"(for +([a-zA-Z_][a-zA-Z_0-9]*))|(([a-zA-Z_][a-zA-Z_0-9]*) *=)")

		for i in name.finditer(programtext):
			if i.group(2):
				print(i.group(2))
			else:
				print(i.group(4))
	else:
		print("Error - file name is invalid")

#############################################################################################
#                                       End of Program                                      #
#                                       Copyright 2019                                      #
#############################################################################################