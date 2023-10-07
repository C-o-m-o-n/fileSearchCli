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
        print("Searching for files...")
        found_files = []
        for dirpath, _, filenames in os.walk(self.rootdir):
            if search_item in filenames:
                found_files.append((dirpath, search_item))

        if found_files:
            for dirpath, filename in found_files:
                print(f"File found: {os.path.join(dirpath, filename)}")
            print(f"Total files found: {len(found_files)}")
            print(f"Time taken: {time.time() - start:.2f} seconds")
        else:
            print(f"No files found with the name '{search_item}'.")

    def search_dir(self, search_item):
        """
        Search for directories with a given name.

        Args:
            search_item (str): The name of the directory to search for.
        """
        start = time.time()
        print("Searching for directories...")
        found_dirs = []
        for dirpath, dirnames, _ in os.walk(self.rootdir):
            if search_item in dirnames:
                found_dirs.append(os.path.join(dirpath, search_item))

        if found_dirs:
            for found_dir in found_dirs:
                print(f"Directory found: {found_dir}")
            print(f"Total directories found: {len(found_dirs)}")
            print(f"Time taken: {time.time() - start:.2f} seconds")
        else:
            print(f"No directories found with the name '{search_item}'.")


if __name__ == "__main__":
    rootdir = input("Enter the root directory path: ")
    option = input("What do you want to search for? [1]: file, [2]: directory: ")
    search_item = input("Enter the search term: ")

    searcher = FileSearch(rootdir)

    if option == '1':
        searcher.search_file(search_item)
    elif option == '2':
        searcher.search_dir(search_item)
    else:
        print("Invalid option. Please choose 1 for files or 2 for directories.")
