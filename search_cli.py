import os
import time

class FileSearch:
    def __init__(self, rootdir):
        """
        Initialize the FileSearch object with the root directory.

        Args:
            rootdir (str): The root directory where the search will start.
        """
        self.rootdir = rootdir

    def search_file(self, search_item):
        """
        Search for files with a given name.

        Args:
            search_item (str): The name of the file to search for.
        """
        start = time.time()
        print("\033[96mSearching for files...\033[0m")  # OKCYAN color
        found_files = []
        for dirpath, _, filenames in os.walk(self.rootdir):
            if search_item in filenames:
                found_files.append((dirpath, search_item))

        if found_files:
            for dirpath, filename in found_files:
                print(f"\033[92mFile found: {os.path.join(dirpath, filename)}\033[0m")  # OKGREEN color
            print(f"\033[92mTotal files found: {len(found_files)}\033[0m")  # OKGREEN color
            print(f"\033[92mTime taken: {time.time() - start:.2f} seconds\033[0m")  # OKGREEN color
        else:
            print(f"\033[91mNo files found with the name '{search_item}'.\033[0m")  # FAIL color

    def search_dir(self, search_item):
        """
        Search for directories with a given name.

        Args:
            search_item (str): The name of the directory to search for.
        """
        start = time.time()
        print("\033[96mSearching for directories...\033[0m")  # OKCYAN color
        found_dirs = []
        for dirpath, dirnames, _ in os.walk(self.rootdir):
            if search_item in dirnames:
                found_dirs.append(os.path.join(dirpath, search_item))

        if found_dirs:
            for found_dir in found_dirs:
                print(f"\033[94mDirectory found: {found_dir}\033[0m")  # OKBLUE color
            print(f"\033[92mTotal directories found: {len(found_dirs)}\033[0m")  # OKGREEN color
            print(f"\033[92mTime taken: {time.time() - start:.2f} seconds\033[0m")  # OKGREEN color
        else:
            print(f"\033[91mNo directories found with the name '{search_item}'.\033[0m")  # FAIL color

if __name__ == "__main__":
    rootdir = input("\033[93mEnter the root directory path: \033[0m")  # WARNING color
    option = input("\033[93mWhat do you want to search for? [1]: file, [2]: directory: \033[0m")  # WARNING color
    search_item = input("\033[96mEnter the search term: \033[0m")  # OKCYAN color

    searcher = FileSearch(rootdir)

    if option == '1':
        searcher.search_file(search_item)
    elif option == '2':
        searcher.search_dir(search_item)
    else:
        print("\033[91mInvalid option. Please choose 1 for files or 2 for directories.\033[0m")  # FAIL color
