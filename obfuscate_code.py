#!/usr/bin/env python
import optparse
from colorama import Style, Fore
import os
import sys
import py_compile
import datetime
import random
import string
import inspect
import shutil


parser = optparse.OptionParser()

parser.add_option('-f', '--file',
    action="store", dest="file",
    help="File to obfuscate", default="")

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

def ask_format():
    frmt_choice = raw_input(color.YELLOW + "(?)" + color.END + " Would you like to save your backdoor as [1]'.py' or [2]'.pyz' or [3]'.pyc'> ")
    if frmt_choice == "1":
        full_file = "obfuscated_payload.py"
        print color.GREEN + "(+)" + color.END + " Saving as .py ..."
        os.rename("TEMP_FILE.pyc", "obfuscated_payload.py")
    elif frmt_choice == "2":
        full_file = "obfuscated_payload.pyz"
        print color.GREEN + "(+)" + color.END + " Saving as .pyz ..."
        os.rename("TEMP_FILE.pyc", "obfuscated_payload.pyz")
    elif frmt_choice == "3":
        full_file = "obfuscated_payload.pyc"
        print color.GREEN + "(+)" + color.END + " Saving as .pyc ..."
        os.rename("TEMP_FILE.pyc", "obfuscated_payload.pyc")
    else:
        print color.RED + "(-)" + color.END + " Invalid Format Choosen..."
        print colr.GREEN + "(+)" + color.END + " Saving as .py, by default.."
        os.rename(options.file, "obfuscated_payload.py")
    if os.path.exists(os.getcwd()+"/final_payloads/"+full_file):
        os.remove(os.getcwd()+"/final_payloads/"+full_file) 
    shutil.move(full_file, "final_payloads")
    print color.YELLOW + "\n< Final File Informations >"
    print color.GREEN + "(+)" + color.END + " File => "+options.file
    print color.GREEN + "(+)" + color.END + " Mode => Obfuscating"
    print color.GREEN + "(+)" + color.END + " Output File => final_payloads/"+full_file

print color.YELLOW + "(i)" + color.END + " Preparing Full Obfuscating" 
print color.GREEN + "(+)" + color.END + " Obfuscating "+options.file+" !..."   
py_compile.compile(options.file, dfile="TEMP_FILE.pyc", cfile="TEMP_FILE.pyc")
print color.GREEN + "(+)" + color.END + " Finished Obfuscation!"
ask_format()
