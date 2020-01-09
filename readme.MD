# Lab 13
https://sites.google.com/site/fiipythonprogramming/laboratories/lab-13

# Exercise 1
Create a function that receives two parameters: a_path and ext. The script will add all files from the a_path folder that have the extension ext to a zip archive named the.zip. Optionally: a third parameter may specify the full archive path.

# Exercise 2
Create a function that receives one parameter: a_path. If a_path is a valid zip archive the function will return a list containing all file names inside. If a_path is not a valid zip archive the function will return False.

# Exercise 3
Create a function that receives two parameters: a_path and to_hextract. If a_path is a valid zip archive and to_hextract  is a file inside the arhive the function will return the md5 digest for unzipped content of to_hextract and None otherwise

#

Consider the sql table files with the following columns:

    file_name             -> text
    parrent_folder  ->  text
    timestamp .         -> text

# Exercise 4
Create a function that receives two parameters: a_path and dbpath. If the database at dbpath already exists it should contain the table files described above if not the table will be created. For every file in a_path the function will insert information  in the table files.

For example if the function is ran at 2020-01-01 01:00:00 for the folder c:\test ( which contains the files a.txt and b.txt ) the function will insert in the table files the following row:

        a.txt , c:\test ,  2020-01-01 01:00:00
        b.txt , c:\test ,  2020-01-01 01:00:00

All changes will be commited

# Exercise 5
Create a function that receives a parameter : dbpath - the path to a database containing a table files ( described above ). The function will return all rows from the table files or an error.
