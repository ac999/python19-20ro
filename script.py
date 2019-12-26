import os

'''
Write a function called search_by_content which has two parameters:
	target and to_search.
The function will return a list of files containing to_search.
If target represents a file, this will be the only file searched.
If target represents a directory, all the files found in the directory
	(recursively) will be searched.
If target does not exist an empty list will be returned.
'''

def search_by_content(target, to_search, _list=[]):
	if os.path.isfile(target):
		for line in open(target):
			if to_search in line.strip():
				_list.append(target)
				break
	if os.path.isdir(target):
		[search_by_content(os.path.join(target,node),to_search) for node in
		os.listdir(target)]
	return _list
print("search_by_content(\".\"):")
print(search_by_content(".", "search_by_content"))
print()

'''
Write a function get_file_info that has one parameter representing a file path.
The function will return a dictionary with the following fields:

- full_path - the absolute path of the file

- file_size - the size of the file

- file_extension - the file's extension

- can_read/can_write - True or False, if the user can read from the file/write
	in the file.

'''

def get_file_info(file_path):
	if not os.path.exists(file_path):
		return dict()
	return dict(
		[
		("full_path", os.path.abspath(file_path)),
		("file_size", os.path.getsize(file_path)),
		("file_extension", os.path.splitext(file_path)[1]),
		("can_read", os.access(file_path, os.R_OK)),
		("can_write", os.access(file_path, os.W_OK))
		]	
	)

print("get_file_info(\"./script.py\"):\n{}".format(get_file_info("./script.py")
	))

'''
Write a function that receives a filename as a parameter and writes the data
from the os.environ in the file given as parameter. Each line containing an
entry in this dictionary, in the form of the key [tab] value.
'''

def ex3(filename):
	file = open(filename,"w+")
	environ=os.environ
	for key in environ:
		file.write("{} : {}\n".format(key,environ[key]))
	file.close()

ex3("environ.txt")

'''
4. Write a function that receives as a parameter a path that represents a
directory on the system. The function will recursively browse the files and
directories at the given path and will display at the console all the paths it
has found and their type (FILE, DIRECTORY, UNKNOWN.
You are NOT allowed to use os.walk.
'''

def get_type(fpath):
	if os.path.isfile(fpath):
		print("{}: FILE;".format(fpath))
		return True
	else:
		if os.path.isdir(fpath):
			print("{}: DIRECTORY;".format(fpath))
			return True
	print("{}: UNKNOWN;".format(fpath))

print("\nex4(\"{}\"):".format("."))

def ex4(_directory="."):
	get_type(_directory)
	if os.path.isdir(_directory):
		[ex4(os.path.join(_directory,node)) for node in
		os.listdir(_directory)]

ex4()

'''
5. Write a function that has 3 parameters: source (a path to a file),
directory (a path to a directory) and buffer_size (an integer).
The function will copy the given file into the given directory, using a buffer
of the third parameter size, in bytes.
'''

print("\nex5({},\"./test\",4096)"
	.format(os.path.abspath(__file__)))
def ex5(source=os.path.abspath(__file__)
	, directory="./test"
	, buffer_size=100):

	if not os.path.exists(directory):
		os.mkdir(directory)

	filename=os.path.basename(source)
	new_file = open("{}/{}".format(directory,filename),"w+")
	old_file = open(source,"r")
	# iteration=0
	while True:
		# iteration+=1
		_buffer=old_file.read(buffer_size)
		new_file.write(_buffer)
		# print("\n ex5 it{}: \n{}".format(iteration, _buffer))
		if not _buffer:
			break
ex5()

'''
6. Write a function which receives a path to a directory as an argument and
returns a dictionary with the following fields:

- full_path - absolute path of the directory

- total_size - the total size of the files found recursively in the directory

- files - a list of relative paths of the files found inside the directory

- dirs - a list of absolute paths to the directories found inside the directroy.
'''

def list_files_get_size(target, size=[], _listfiles=[], _listdirs=[]):
	if os.path.isfile(target):
		_listfiles.append(target)
		size.append(os.path.getsize(target))
	if os.path.isdir(target):
		_listdirs.append(target)
		[list_files_get_size(os.path.join(target,node)) for node in
		os.listdir(target)]
	return sum(size), _listfiles,_listdirs

def ex6(_dir):
	_dict={"full_path": os.path.abspath(_dir)+"/"+_dir}
	_dict["total_size"],_dict["files"],_dict["dirs"]=list_files_get_size(_dir)
	return _dict

print("\nex6(\".\"):\n")
print(ex6("."))

'''
8. Write a function that has the following parameters:
path, tree_depth, filesize, filecount, dircount and create a directory
structure as follows: starting from the root path it will create <dircount>
directories and <filecount> files. Each file will have a size equal
to <filesize>. This process will be repeated recursively for each created
directory until the desired depth is reached - no directories will be created
for the directories on the last level.
'''

def touch(file,size):
	f = open(file,"w+b")
	f.seek(size-1)
	f.write(b"\0")
	f.close()

def create_dummy_tree(path="./dummy_tree", tree_depth=2, filesize=1024, filecount=3
	, dircount=3):
	if tree_depth>1:
		for i in range(dircount):
			new_dir="{}/dir{}".format(path,i)
			os.mkdir(new_dir)
			create_dummy_tree(new_dir,tree_depth-1,filesize,filecount,dircount)
	for i in range(filecount):
		touch("{}/file{}".format(path,i),filesize)

create_dummy_tree()
