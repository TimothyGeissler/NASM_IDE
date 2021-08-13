import time
from subprocess import call
import sys

proj_name = sys.argv[1]
output_name = ""


def build():
    global output_name
    output_name = input("Enter executable name: ")
    print("Assembling " + proj_name + "...")
    try:
        call(["nasm", "-f", "elf", proj_name + ".asm"])
        print("Assembled " + proj_name + ".o\nCompiling executable " + output_name + "...")
        call(["ld", "-m", "elf_i386", "-s", "-o", output_name, proj_name + ".o"])
        print("Compiled Successfully: " + output_name)
    except:
        print("NASM package not found or not in PATH")
    menu()


def run():
    print("Running executable: " + output_name + "\n")

    # print("gnome-terminal -- /bin/bash -c \"./" + output_name + ";bash\"")
    time.sleep(2)
    # gnome-terminal -x sh -c './built; exec bash'
    # call(["gnome-terminal", "-x", "-sh", "-c", "'./" + output_name + "; exec bash\'"])
    call(["./" + output_name])
    menu()


def menu():
    print("\n\n~~~~~NASM Builder by T.Geissler~~~~~\nTarget: " + proj_name + ".asm\n")
    input_cmd = input("Enter [b] to build, [r] to run, [e] to exit...")
    if input_cmd == 'b':  # build w/ nasm
        build()
    if input_cmd == 'r':
        run()
    if input_cmd == 'e':
        sys.exit()

menu()
