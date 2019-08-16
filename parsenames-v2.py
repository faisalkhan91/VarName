#!/usr/local/bin/python3


#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               Email: faisalkhan91@outlook.com                             #
#                               Date: 8/16/2019                                              #
#############################################################################################

# Importing system module

import re
import sys
import os

namedict = {}


def forsub(matchobj):
	
	name = matchobj.group(1)
	namedict[name] = "loopvariable"

	return "for loopvariable"


def forsub2(matchobj):

	if matchobj.string[:matchobj.start()].count('"') % 2 == 0 and matchobj.string[matchobj.end():].count('"') % 2 == 0:
		return matchobj.group(1)+"loopvariable"+matchobj.group(2)
	else:
		return matchobj.group(0)


def normalsub(matchobj):
	
	name = matchobj.group(1)
	namedict[name] = "normalvariable"

	return "normalvariable ="


def normalsub2(matchobj):

	if matchobj.string[:matchobj.start()].count('"') % 2 == 0 and matchobj.string[matchobj.end():].count('"') % 2 == 0:
		return matchobj.group(1)+"normalvariable"+matchobj.group(2)
	else:
		return matchobj.group(0)


if len(sys.argv) != 2:
	print("Error - must supply name of program to search")
else:
	if os.path.isfile(sys.argv[1]):
		programfile = open(sys.argv[1])
		programtext = programfile.readlines()
		programfile.close()

		forname = re.compile(r"for +([a-zA-Z_][a-zA-Z_0-9]*)")
		normalname = re.compile(r"([a-zA-Z_][a-zA-Z_0-9]*) *=")

		newtext = []

		for line in programtext:
			newline = forname.sub(forsub, line)
			newline = normalname.sub(normalsub, newline)
			newtext.append(newline)

		for line in newtext:
			for name, type in namedict.items():
				nameexp = re.compile(r"([^a-zA-Z])"+name+r"([^a-zA-Z])")
				
				if type == "loopvariable":
					line = nameexp.sub(forsub2, line)
				else:
					line = nameexp.sub(normalsub2, line)
			print(line, end="")
	else:
		print("Error - file name is invalid")

#############################################################################################
#                                       End of Program                                      #
#                                       Copyright 2019                                      #
#############################################################################################
