########################### Paths ######################

from pathlib import Path

# creating an absolute path on windows

path1 = Path("C:\\Program Files\\Python3")
print(path1)


# using raw string to simplify the path creation

path2 = Path(r"C:\Program Files\Python 3")
print(path2)

# relative paths
path3 = Path("users/__init__.py")
print(path3)

# a path() object that represents the current folder
path4 = Path()
print(path4)

# combining Path() objects together
path5 = Path("Some_Path") / Path("users")
print(path5)

# combining a Path() object with a string
path6 = Path("some_file") / "ecommerce" / "__init__.py"
print(path6)


# Getting the home directory of the current user
print(Path.home())

# calling the exists method to find out if the file or directory exists or not
path7 = Path("social/audio")
path8 = Path("social/images/__init__.py")
path9 = Path("users")


print(path7.exists())
print(path8.exists())
print(path9.exists())

# to check to see if this path is a file

print(path7.is_file())
print(path8.is_file())
print(path9.is_file())

# to check to see if this path is a directory

print(path7.is_dir())
print(path8.is_dir())
print(path9.is_dir())

# extracting individual components in this path
# returns the file name in path
print(path7.name)
print(path8.name)
print(path9.name)


# extracting individual components in this path returns the file name in path without the extension

print(path7.suffix)
print(path8.suffix)
print(path9.suffix)

# extracting individual components in this path return the patent of the file

print(path7.parent)
print(path8.parent)
print(path8.parent)

# creates a new path with the file name changed
path10 = path7.with_name("__initialization__.txt")
print(path10)

# getting the absolute path for the newly created file
print(path7.absolute)

# change the extension of a file
path11 = path9.with_suffix(".js")
print(path11)
