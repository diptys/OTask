'''how to check empty files and directories in folder with functions'''


'''import os
import io
x=input("enter path:")
f=open("empty.txt","w")
if __name__ == "__main__":
    lst = os.walk(x, topdown=True)

    for (root,dirs,files)in lst:
        if (len(root) > 0 and len(dirs) == 0 and len(files) == 0):
            print(root)
            f.write(root)
            print(dirs)
            print(files)
            print("files are not there...")
            print('--------------------------------')

f.close()
'''


import os
import io
#x = input("enter path:")

def ls(lst):
    f = open("empty.txt", "w")
    for (root, dirs, files) in lst:
        if (len(root) > 0 and len(dirs) == 0 and len(files) == 0):
            print(root)
        f.write(root)
        print(root)
        print(dirs)
        print(files)
        print("files are not there...")
        print('--------------------------------')
    f.close()

def method():
    #option2search=1
    lst = os.walk("x", topdown=True)
    ls(lst)

method()
