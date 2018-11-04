#!/usr/bin/env python
import optparse
from colorama import Style, Fore
import os
import sys
import py_compile
import datetime
import random
import string
import base64
import shutil
import time

parser = optparse.OptionParser()

parser.add_option('-f', '--file',
    action="store", dest="file",
    help="File to Compile (.exe)", default="")

options, args = parser.parse_args()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print color.YELLOW + "(i)" + color.END + " Compiling "+options.file+" to exe ..."
os.system("wine pyinstaller -n compiled_payload --onedir --onefile "+options.file)
print color.GREEN + "(+)" + color.END + " Finish to compile to exe!"
print color.YELLOW + "(i)" + color.END + " Cleaning up our mess..."
if os.path.exists("compiled_payload.spec"):
    os.remove("compiled_payload.spec")
if os.path.isdir("build"):
    shutil.rmtree("build")

shutil.move(os.getcwd()+"/dist/compiled_payload.exe", os.getcwd()+"/")
shutil.rmtree("dist")
print color.GREEN + "(+)" + color.END + " Finished Cleaning up our mess!"

if os.path.exists(os.getcwd()+"/final_payloads/compiled_payload.exe"):
    os.remove(os.getcwd()+"/final_payloads/compiled_payload.exe")
shutil.move("compiled_payload.exe", "final_payloads")
print color.YELLOW + "\n< Final File Informations >"
print color.GREEN + "(+)" + color.END + " File => "+options.file
print color.GREEN + "(+)" + color.END + " Mode => Encode - Base64"
print color.GREEN + "(+)" + color.END + " Output File => final_payloads/compiled_payload.exe"
