"""

"""


from datetime import datetime
import time
import os



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



#start time
start = time.strftime('%S')
rootdir = '/' #for kali linux
# rootdir = '/data/data/com.termux' #for termux
option = input(bcolors.WARNING + "what do you want to search for?[1]:file ,[2]:directory : ")
search_item = input(bcolors.OKCYAN + '+++++[SEARCH]:\t')
time.sleep(2)
class FileSearch(bcolors):
    def __init__(self):
        pass
    def search_file(self, search_item):
        print(bcolors.OKCYAN + "searching.........")	
        for dirpaths, dirnames, filenames in os.walk(rootdir):
            if search_item in filenames:
                print(bcolors.OKGREEN + "+++[FILES IN THAT DIRECTORY] :", filenames, '\n')
                print(bcolors.OKGREEN+'+++[TO THE DIRECTORY] :', os.path.join(dirpaths, search_item), '\n')
                stop = time.strftime('%S')
                print(bcolors.OKGREEN + '+++[ATTEMPTS] :', len(dirpaths), '\n')
                print(bcolors.OKGREEN + '+++[TIME] :', int(stop)-int(start), ' seconds\n')
                print(bcolors.HEADER + '\n+++++++++++++++++++++++++++++++++++++\n')
	
    def search_dir(self, search_item):
        print(bcolors.OKGREEN + "\nsearching.........\n")	
        time.sleep(2)
        for dirpaths, dirnames, filenames in os.walk(rootdir):
            if search_item in dirnames:
                stop = time.strftime('%S')
                print(bcolors.OKBLUE + '+++[PATH] :' , os.path.join(dirpaths, search_item), '\n')
                print(bcolors.OKGREEN + '+++[TIME] :', int(stop)-int(start), 'seconds\n' )
                print(bcolors.OKGREEN + '+++[ATTEMPTS] :',len(dirpaths), '\n')
                print(bcolors.HEADER + '\n+++++++++++++++++++++++++++++++++++++\n')


searcher = FileSearch()

if __name__ == "__main__":
    if option == '1':
        searcher.search_file(search_item)
    elif option == '2':
        searcher.search_dir(search_item)



