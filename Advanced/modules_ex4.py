import os
from datetime import datetime

#create folder
if os.path.exists("test"):
    print("test folder exists")
else:
    os.mkdir("test")
    print("test folder created")


folder= 'a/b/c/d/e/f/g'
if os.path.exists(folder):
    print("path exist")
else:
    os.makedirs(folder)
    print("path created")


# delete a file
if os.path.exists("faltu.txt"):
    os.unlink("faltu.txt")
    print("faltu.txt deleted")
else:
    print("faltu.txt does not exist")


# delete a folder
if os.path.exists("test"):
    os.rmdir("test")
    print("test folder deleted")
else:
    print("test folder does not exist")

#     # display details

if os.path.exists("basics/hello.py"):
    size=os.path.getsize('basics/hello.py')
    ctime=os.path.getctime("basics/hello.py")
    mtime=os.path.getmtime("basics/hello.py")
    isfile=os.path.isfile("basics/hello.py")
    isdir=os.path.isdir("basics/hello.py")
    print('filename: basic/hello.py')
    print('size:', size,'bytes')
    print("ctime:" , datetime.fromtimestamp(ctime))
    print("mtime:" , datetime.fromtimestamp(mtime))
    print("file h ye ? " , isfile)
    print("folder h ye?" ,isdir)
    

# recursive display file tree

print("recursive display  file tree")
for root,dirs,files in os .walk('.'):
    print(f"folder is {root.upper()}")
    print("total folders:",len(dirs))
    print("files in this folder are:",files)
