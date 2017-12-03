'''
Create a program that automates part of writing unit tests
Unlike test_generator.py, it does not use print but format()
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

'{0}'.format('import unittest \n')

'{0}'.format('class Test(unittest.TestCase):')
	
for i in range(len(L)):
	for i in range(len(L)):
	' def test_{0} self:'.format(L[i])
	print('\n')

print('unittest.main()')
