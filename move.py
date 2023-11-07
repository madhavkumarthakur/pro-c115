import os
source="main.txt"
dest='newmain.txt'
os.rename(source,dest)
print("source file renamed to destination path successfully")