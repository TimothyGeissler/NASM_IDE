# import os
# os.system("df")

from subprocess import call

proj_name = input("Enter project name: ")
call(["gnome-terminal", "-x", "python3", "builder.py", proj_name])
call(["sudo", "nano", proj_name + ".asm"])
# call(["ls", "-l"])
