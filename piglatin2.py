#!usr/local/bin/python3.6
''' Write a module piglatin containing a to_piglatin() function'''
import argparse

def to_piglatin(string):
	L=[]
	for i in string:
		for j in ['a','e','i','o','u','y']:
			if j == i:
				L+=[i]
	string = L[0] + string[string.index(L[0])+1:] + string[0:string.index(L[0])] + 'ay'
	return string

parser = argparse.ArgumentParser(description = 'piglatin conversion of words in a file')

parser.add_argument('-file','--file', type = str, help='convert every words in this file in piglatin way')

args = parser.parse_args()
mon_fichier = open(args.file,"r")
s=''
for line in mon_fichier:
	s=to_piglatin(line.rstrip('\n'))
	print(s)

mon_fichier.close()

