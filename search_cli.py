from datetime import datetime
import time
import os

"""
for linux
"""

#start time
start = time.strftime('%S')
#rootdir = '/' #for kali linux
rootdir = '/data/data/com.termux' #for termux
search_item = input('+++++[SEARCH]:\t')
time.sleep(2)
class Os_seer:
	def __init__(self):
		pass
	def search_file(self, search_item):
		print("searching.........")	
		for dirpaths, dirnames, filenames in os.walk(rootdir):
			if search_item in filenames:
				print("+++[FILES] :", filenames, '\n')
				print('+++[PATH] :', os.path.join(dirpaths, search_item), '\n')
				stop = time.strftime('%S')
				print('+++[ATTEMPTS] :', len(dirpaths), '\n')
				print('+++[TIME] :', int(stop)-int(start), ' seconds\n')
				print('\n+++++++++++++++++++++++++++++++++++++\n')
	
	def search_dir(self, search_item):
		print("\nsearching.........\n")	
		time.sleep(2)
		for dirpaths, dirnames, filenames in os.walk(rootdir):
			if search_item in dirnames:
				stop = time.strftime('%S')
				print('+++[PATH] :' , os.path.join(dirpaths, search_item), '\n')
				
				print('+++[TIME] :', int(stop)-int(start), 'seconds\n' )
				
				print('+++[ATTEMPTS] :',len(dirpaths), '\n')
				
				print('\n+++++++++++++++++++++++++++++++++++++\n')


osSeer = Os_seer()
#this only works if the search_item  is in the same directory
#changes are still being made
if os.path.isfile(search_item):
  print("\nDetected a file......\n")
  osSeer.search_file(search_item)
elif os.path.isdir(search_item):
  print("\nDetected a directory......\n")
  osSeer.search_dir(search_item)



