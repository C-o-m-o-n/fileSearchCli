# FileSearchCli
- A python script that helps you search files and directories in the terminal  


## How the code works 
GitHub Copilot: The active selection is a Python script that searches for files and directories in a given root directory. The script defines a `FileSearch` class that takes the root directory as an argument and has two methods: `search_file` and `search_dir`. The `search_file` method searches for files with a given name in the root directory and its subdirectories, while the `search_dir` method searches for directories with a given name in the same location. 

The script uses the `os` and `time` modules to perform the search and measure the time taken. The `os.walk` method is used to traverse the directory tree and find the files and directories. The search results are stored in lists and printed to the console using colored text to distinguish between files and directories found and to indicate success or failure of the search. 

The script prompts the user to enter the root directory path, the type of search to perform (files or directories), and the search term. It then creates an instance of the `FileSearch` class with the root directory path and calls the appropriate search method based on the user's choice. If an invalid option is entered, an error message is printed to the console. 

To improve the readability of the code, the `search_file` and `search_dir` methods could be refactored to reduce code duplication. Additionally, the use of colored text could be replaced with logging statements to make the output more flexible and easier to read. To improve performance, the script could use multi-threading or multiprocessing to search for files and directories in parallel.
GitHub Copilot: The active selection is a Python script that searches for files and directories in a given root directory. The script defines a `FileSearch` class that takes the root directory as an argument and has two methods: `search_file` and `search_dir`. The `search_file` method searches for files with a given name in the root directory and its subdirectories, while the `search_dir` method searches for directories with a given name in the same location. 

The script uses the `os` and `time` modules to perform the search and measure the time taken. The `os.walk` method is used to traverse the directory tree and find the files and directories. The search results are stored in lists and printed to the console using colored text to distinguish between files and directories found and to indicate success or failure of the search. 

The script prompts the user to enter the root directory path, the type of search to perform (files or directories), and the search term. It then creates an instance of the `FileSearch` class with the root directory path and calls the appropriate search method based on the user's choice. If an invalid option is entered, an error message is printed to the console. 

To improve the readability of the code, the `search_file` and `search_dir` methods could be refactored to reduce code duplication. Additionally, the use of colored text could be replaced with logging statements to make the output more flexible and easier to read. To improve performance, the script could use multi-threading or multiprocessing to search for files and directories in parallel.

---
## Installation

- clone this git repository

        bash
        git clone https://github.com/C-o-m-o-n/fileSearchCli


## Usage

> ### cd fileSearchCli
>> `python search_cli.py`
>> #### chose to search a file or directory
>> #### [SEARCH]: 1 for searching files
>>  #### [SEARCH]: 2 for searching directories


## Termux
> #### for termux users, change the `rootdir` to `'/data/data/com.termux'`
>>  rootdir = 'data/data/com.termux'  

# contributions
> #### your contributions wii be highly appreciated
