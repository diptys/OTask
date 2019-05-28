import shutil
import os

SRC = "/home/automaton/Desktop/sumati"
DES = "/home/automaton/Desktop/55"
def ig_f(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]

shutil.copytree(SRC, DES, ignore=ig_f)