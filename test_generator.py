'''
Create a program that automates part of writing unit tests
'''
#!usr/local/bin/python3.6

def getListofFunction(moduleName):
	''' function that inspect a module in order to get all the functions in it'''
	L1 = []	
	import importlib, inspect
	mod_to_test = importlib.import_module(moduleName)
	L = inspect.getmembers(mod_to_test)
	for function, namespace in L:
		if function[0]!='_':
			L1+=[function]
	return L1

L = getListofFunction("piglatin")

print('import unittest \n')

print('class Test(unittest.TestCase):')
	
for i in range(len(L)):
	print(' ','def','test_',end = '')
	print(L[i],'(self):', sep='')
	print('\n')

print('unittest.main()')
