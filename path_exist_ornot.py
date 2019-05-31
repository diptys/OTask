'''check a list of path is exist or not'''

import os
import io
#from pathlib import Path
x=input("enter path:")
f=open(x)
line=f.readline()

while line != "":
    line=line.rstrip()
    if os.path.exists(line):
        print("path is exist")
    else:
        print("path is not exist")
    print(line)
    line= f.readline()
