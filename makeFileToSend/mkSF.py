import os
import shutil
import subprocess
import fileinput
import tkinter.messagebox

projP = os.getcwd()
projP += '/'
cmake = projP + 'CMakeLists.txt'
fileF = "sendF.cpp"
with open(cmake, 'r') as f:
    for l in f:
        if l[0:14] ==  "add_executable":
            fileF = l.split()[1][:-1]
fileF = projP + fileF
sendF = projP + "..cpp"
try:
    shutil.copy(fileF, sendF)
except Exception as e:
    tkinter.messagebox.showerror("Error", "file creation crashed")
    exit(0)
try:
    subprocess.run(["clang-format", "-i", "-Werror", sendF])
except Exception as e:
    tkinter.messagebox.showerror("Error", "clang fucked up\n"+str(e))
    exit(0)
with fileinput.input(sendF, inplace=1) as f:
    for l in f:
        if l[:7] == "#define":
            l = "# " + l[1:]
        print(l, end="")