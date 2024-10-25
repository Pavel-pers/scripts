import sys
import os
import tkinter
import tkinter.messagebox
import subprocess

cur_path = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) < 2:
    tkinter.messagebox.showerror("Error", "No filename specified")
    sys.exit(0)

if len(sys.argv) > 2:
    tkinter.messagebox.showwarning("Warning", "Too many arguments")

path = open(cur_path + '/data/samples_path.txt', 'r').read()
name = sys.argv[1]

filepath = path + name + ".cpp"

if os.path.exists(filepath):
    tkinter.messagebox.showerror("Error", "File already exists")
    sys.exit(0)

samplefile_path = cur_path + '/data/sample.cpp'
with open(filepath, "w") as out, open(samplefile_path, 'r') as inp:
    for line in inp:
        out.write(line.replace("%%name%%", name))

inpPath = path + name + '.in'
outpPath = path + name + '.out'
open(inpPath, "w").close()
open(outpPath, "w").close()

try:
    com = subprocess.run(["code", filepath, inpPath, outpPath])
except Exception as e:
    tkinter.messagebox.showerror("Error", "Editor command failed")
