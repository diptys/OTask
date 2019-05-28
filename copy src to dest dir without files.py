import shutil
import os

def ig_f(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]
def copy_tree_structure(SRC,DES):
    shutil.copytree(SRC, DES,ignore=ig_f)

def main():
    SRC = input("enter srcdir path:")
    DES = input("enter destdir path:")
    copy_tree_structure(SRC,DES)

if __name__ == "__main__":
	main()