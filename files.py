import collections
from pathlib import Path
my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in my_files:
    print(Path(r'C:\Users\User'),filename)

# Joining Paths
# The '/' operator is used to join paths
# The only thing to keep in mind while using the '/' operator for joining paths is that on of the first two values in the expression must be a Path object.
print(Path('spam')/'bacon'/'eggs')
print(Path('spam')/Path('bacon/eggs'))
print(Path('spam')/Path('bacon','eggs'))

# Accessing the Current Working Directory
# We can get the current working directory as a string value with the Path.cwd()
print(Path.cwd())

# Accessing the Home Directory
# The Path.home() method returns a new path object that points to the user's home directory.
print(Path.home())

# A single period (dot) for a folder name is shorthand for this folder.
# Two periods (dot-dot) means the parent folder.

# Creating New Folders
# The Path.mkdir() method can be used to create a new folder.
# Path("emails").mkdir()
# The Path.mkdir() method can also be used to create nested folders.
# Path("emails\processed").mkdir()

# Calling the is_absolute() method on a Path object will return True if it represents an absolute path or False if it represents a relative path.
my_file=Path.home() / "Documents"
print(my_file.is_absolute())
# To get an absolute path from a relative path, you can put Path.cwd() / in front of the relative Path object.
print(Path.cwd() / "emails")

print()
# Finding File Sizes and Timestamps
# The `stat()` method return a stat_result object with file size and timestamp information about a file.
strings_file = Path('strings.py')
print(strings_file.stat())
import time
print(time.asctime(time.localtime(strings_file.stat().st_mtime)))

print()
# Finding Files using Glob Patterns
# '*.txt' matches all files that end with .txt.
# 'project?.txt' matches 'project1.txt', 'project2.txt', or 'projectX.txt'.
# '*project?.*' matches 'catproject5.txt' or 'secret_project7.docx'.
# '*' matches all filenames.
p = Path.cwd()
for name in p.glob('*'):
    print(name)

# Checking Path Validity
"""
Assuming that a variable `p` holds a `Path` object, we could expect the following:
1. Calling `p.exists()` return True if the path exists, and return False if it doesn't exist.
2. Calling `p.is_file()` returns True if the path exists and is a file, and return False otherwise.
3. Calling `p.is_dir()` returns True if the path exists and is a directory, and return False otherwise.
"""
print()
print(p.exists())
print(p.is_dir())
print(p.is_file())
print()

# The file reading and writing process
# The pathlib module’s read_text() method returns the full contents of a text file as a string.
# Its write_text() method creates a new text file (or overwrites an existing one) with the string passed to it.
p = Path('test.txt')
p.write_text('This is a testing file.')
print(p.read_text())

# Opening Files
test_file = open(Path.cwd()/'test.txt', encoding='UTF-8')
# The open() function will open the file in “reading plaintext” mode, or read mode for short.
# The call to open() returns a File object.
# A File object represents a file on your computer.

# Reading the Contents of Files
test_content = test_file.read()
print()
print(test_content)
# We can use the readlines() method to get a list fo string values from the file, one for each line of text.
print(test_file.readlines())

# Writing to Files
test_file = open('test.txt', 'w', encoding='UTF-8')
test_file.write('\nHello, World\n')
test_file.close()

# Appending to Files
test_file = open('test.txt', 'a', encoding='UTF-8')
test_file.write('Yeahhhh\n')
test_file.close()

test_file = open('test.txt', encoding='UTF-8')
print(test_file.read())

# Using with statement
with open('test.txt', 'w', encoding='UTF-8') as file:
    file.write('hello, World')
with open('test.txt', encoding='UTF-8') as file:
    print(file.read())

# Saving Variables with the shelve Module
"""
You can save variables in your Python programs to binary shelf files using the shelve module
This lets your program restore that data to the variables the next time it is run.
You could use this technique to add Save and Open features to your program; for example, if you ran a program and entered some configuration settings, you could save those settings to a shelf file and then have the program load the settings the next time it is run.
"""
import shelve
shelf_file = shelve.open('mydata')
shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon']
shelf_file.close()

shelf_file = shelve.open('mydata')
print(type(shelf_file))
print(shelf_file['cats'])
shelf_file.close()