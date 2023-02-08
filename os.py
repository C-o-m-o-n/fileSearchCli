from datetime import datetime
import time
import os

"""
for linux
"""

#start time
start = time.strftime('%S')
rootdir = '/'


search_item = input('...[SEARCH]:  ')

class Os_seer:
	def __init__(self):
		pass
	def search_file(self, search_item):
		print("searcging.........")	
		for dirpaths, dirnames, filenames in os.walk(rootdir):
			if search_item in filenames:
				print("files: \n", filenames)
				print("parth: \n", os.path.join(dirpaths, search_item))
				stop = time.strftime('%S')
				print('i found  ', 'at \n', dirpaths,  '  after ', len(dirpaths), 'attempts', ' and ', int(stop)-int(start) ,' seconds\n')
				
	def search_dir(self, search_item):
		print("searcging.........")	
		for dirpaths, dirnames, filenames in os.walk(rootdir):
			if search_item in dirnames:
				stop = time.strftime('%S')
				print('i found  it ', 'at \n', dirpaths,  '  after ', len(dirpaths), 'attempts', ' and ', int(stop)-int(start) ,' seconds\n')
				  

osSeer = Os_seer()

#osSeer.search_file(search_item)

osSeer.search_dir(search_item)
