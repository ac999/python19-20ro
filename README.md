# Exceptions, Modules (sys and os), I/O, File management
https://sites.google.com/site/fiipythonprogramming/laboratories/lab-9

# Exercise 1
Write a function called search_by_content which has two parameters: target and to_search. The function will return a list of files containing to_search. If target represents a file, this will be the only file searched. If target represents a directory, all the files found in the directory (recursively) will be searched. If target does not exist an empty list will be returned.

# Exercise 2
Write a function get_file_info that has one parameter representing a file path. The function will return a dictionary with the following fields:

- full_path - the absolute path of the file

- file_size - the size of the file

- file_extension - the file's extension

- can_read/can_write - True or False, if the user can read from the file/write in the file.

# Exercise 3
Write a function that receives a filename as a parameter and writes the data from the os.environ in the file given as parameter. Each line containing an entry in this dictionary, in the form of the key [tab] value.

# Exercise 4
Write a function that receives as a parameter a path that represents a directory on the system. The function will recursively browse the files and directories at the given path and will display at the console all the paths it has found and their type (FILE, DIRECTORY, UNKNOWN. You are NOT allowed to use os.walk.

# Exercise 5
Write a function that has 3 parameters: source (a path to a file), directory (a path to a directory) and buffer_size (an integer). The function will copy the given file into the given directory, using a buffer of the third parameter size, in bytes.

# Exercise 6
Write a function which receives a path to a directory as an argument and returns a dictionary with the following fields:

- full_path - absolute path of the directory

- total_size - the total size of the files found recursively in the directory

- files - a list of relative paths of the files found inside the directory

- dirs - a list of absolute paths to the directories found inside the directroy.

# Exercise 7
Write a function that parses a given archive and extracts the files with a certain extension.

The function will have two parameters - container_path (a string representing the path of the container) and extension (a string representing the extension we are looking for).

The container has the following format:

- Starts with the string "CONTAINER"

- The following byte represents the number of files in the archive

- After the previously mentioned byte, for each file there will be

    -> 4 - unsigned integer, little endian bytes representing the size.

    -> 50 bytes representing the file name. (if the name has less than 50 characters, it will be padded with whitespaces)

    -> The body of the file

Test file: https://we.tl/t-FQFRxzaMjf

# Exercise 8
Write a function that has the following parameters: path, tree_depth, filesize, filecount, dircount and create a directory structure as follows: starting from the root path it will create <dircount> directories and <filecount> files. Each file will have a size equal to <filesize>. This process will be repeated recursively for each created directory until the desired depth is reached - no directories will be created for the directories on the last level.


Example: create_dummy_tree('test', 2, 1024, 3, 3) the following structure will be created in the current directory:

    test

    test / dir0

    test / dir0 / file1 (size 1024)

    test / dir0 / file2 (size 1024)

    test / dir0 / file3 (size 1024)

    test / dir1

    test / dir1 / file1 (size 1024)

    test / dir1 / file2 (size 1024)

    test / dir1 / file3 (size 1024)

    test / dir2

    test / dir2 / file1 (size 1024)

    test / dir2 / file2 (size 1024)

    test / dir2 / file3 (size 1024)

    test / file0 (size 1024)

    test / file1 (size 1024)

    test / file2 (size 1024)
