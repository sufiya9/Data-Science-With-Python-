import os

print('current folder')
print(os.getcwd())
print(os.listdir())

print('C drive content')
os.chdir('D:\\')
print(os.getcwd())
print(os.listdir())

address=r'C:\program files\python\python data science.exe'
if os.path.exists(address):
    print('file exists')
else:
    print('file does not exists')
