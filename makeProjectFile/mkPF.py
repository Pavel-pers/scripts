import os
import sys
import fileinput
import shutil
import tkinter.messagebox

projP = os.getcwd()

fileN = sys.argv[1] + ".cpp"
cmake = projP + "/CMakeLists.txt"

try:
    shutil.copy('main.cpp', fileN)
except Exception as e:
    tkinter.messagebox.showerror("Error", "file creation fucked up(main.cpp is crashed probably)")
    exit(0)

try:   
    with fileinput.input(cmake, inplace=1) as f:
        for l in f:
            if l[0:14] == "add_executable":
                print(l.split()[0] + ' '+ fileN + ')', end='')
            else:
                print(l, end='')
except Exception as e:
    tkinter.messagebox.showerror("Error", "couldn't change cmake")
    exit(0)