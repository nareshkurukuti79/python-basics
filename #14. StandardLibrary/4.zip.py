######################  Zip Files ########################

from pathlib import Path

from zipfile import ZipFile

# 1- Creating zip files
all_z = ZipFile("zip_dir/all.zip", "w")
py_z = ZipFile("zip_dir/py.zip", "w")


print(all_z)
print(type(all_z))


# 2 - Adding Files to Zip Files (zipping files)
for path in Path("social").rglob("*.*"):
    all_z.write(path)
all_z.close()


# 3 - Adding Files to Zip Files (zipping files) Approach Two

with ZipFile("zip_dir/py.zip", "w") as py_files:
    for path in Path("social").rglob("*.py"):
        py_files.write(path)

# 4 - showing all files
with ZipFile("zip_dir/all.zip") as all_files:
    print(all_files.namelist())

# 5 - generating a single file's info
with ZipFile("zip_dir/py.zip") as file_info:
    info = file_info.getinfo("social/social.py")
    print(info.file_size)
    print(info.compress_size)
    print(info.orig_filename)
    print(info.__module__)

# 6 - Extracting zip files

with ZipFile("zip_dir/all.zip") as all_file_z:
    all_file_z.extractall("Extracted")
