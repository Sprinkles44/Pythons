#!/usr/bin/python3

usr = input('Please input a string for interpretation: ')
flag = 0
n = len(usr)
if n > 0:
	for i in range(n):
		if usr[i] == 'A':
			word = 'S'
		elif usr[i] == 'B':
			word = 'S'
		elif usr[i] == 'b':
			word = 'T'
		elif usr[i] == 'A' and word == 'T':
			word = 'T'
		elif usr[i] == 'B' and word == 'T':
			word = 'T'
		elif usr[i] == 'b' and word == 'T' or usr[i] == ';':
			flag = 0
			break
		else:
			flag = 1
			break

if flag == 0:
	print("Acceptable")
elif flag == 1:
	print("Unacceptable")