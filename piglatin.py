#!usr/local/bin/python3.6
''' Write a module piglatin containing a to_piglatin() function'''
def to_piglatin(string):
	L=[]
	for i in string:
		for j in ['a','e','i','o','u','y']:
			if j == i:
				L+=[i]
	string = L[0] + string[string.index(L[0])+1:] + string[0:string.index(L[0])] + 'ay'
	return string
