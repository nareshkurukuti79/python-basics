########################## Directories ######################
from pathlib import Path

my_directory = Path("real_estate")
new_directory = Path("social")


# 1-exists() checking whether or not the directory exists
print(my_directory.exists())

# 2-mkdir() creating the directory
# my_directory.mkdir()

# 3-rmdir() removeing directory
# my_directory.rmdir()

# 4-rename() renaming the directory
# my_directory.rename("property_dealer")

# 5-iterdir() getting the list of files and directories at this path

print(new_directory.iterdir())

for data in new_directory.iterdir():
    print(data)

# 6-is_file getting only the files
social_data = [data for data in new_directory.iterdir() if data.is_file()]
print(social_data)

# 7-is_dir() getting only the directories
# social_data = [data for data in new_directory.iterdir() if data.is_dir()]
# print(social_data)

# case1: searching using a patter using the asterisk symbol(*)
paths = [data for data in new_directory.iterdir() if data.is_dir()]

python_files = [data for data in new_directory.glob("*.")]
print('output case1')
print(paths)
print(python_files)

# case2: searching recursively using rglob() method
python_files = [data for data in new_directory.rglob("*.py")]
print(python_files)
python_files = [data for data in new_directory.rglob("*.*")]
print(python_files)
