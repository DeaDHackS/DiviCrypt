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

parser = optparse.OptionParser()

parser.add_option('-f', '--file',
    action="store", dest="file",
    help="File to encode", default="")

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
        full_file = "encoded_payload.py"
        print color.GREEN + "(+)" + color.END + " Saving as .py ..."
        os.rename("encoded_payload.py", "encoded_payload.py")
    elif frmt_choice == "2":
        full_file = "encoded_payload.pyz"
        print color.GREEN + "(+)" + color.END + " Saving as .pyz ..."
        os.rename("encoded_payload.py", "encoded_payload.pyz")
    elif frmt_choice == "3":
        full_file = "encoded_payload.pyc"
        print color.GREEN + "(+)" + color.END + " Saving as .pyc ..."
        os.rename("encoded_payload.py", "encoded_payload.pyc")
    else:
        print color.RED + "(-)" + color.END + " Invalid Format Choosen..."
        print colr.GREEN + "(+)" + color.END + " Saving as .py, by default.."
        os.rename(options.file, "encoded_payload.py")
    
    if os.path.exists(os.getcwd()+"/final_payloads"+"/"+full_file):
        os.remove(os.getcwd()+"/final_payloads"+"/"+full_file)
    shutil.move(full_file, "final_payloads")
    print color.YELLOW + "\n< Final File Informations >"
    print color.GREEN + "(+)" + color.END + " File => "+options.file
    print color.GREEN + "(+)" + color.END + " Mode => Encode - Base64"
    print color.GREEN + "(+)" + color.END + " Output File => final_payloada/"+full_file

print color.YELLOW + "(i)" + color.END + " Encoding "+options.file+" into Base64 ..."
data = open(options.file, "r").read()
encoded = base64.b64encode(data)
print color.GREEN + "(+)" + color.END + " Done! Script source code encoded into Base64!"
print color.GREEN + "(+)" + color.END + " Final Enocoded Payload "+options.file+"!"
print encoded
f = open("encoded_payload.py","w+")
f.write("import base64,sys;exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}[sys.version_info[0]]('"+encoded+"')))")
f.close()
ask_format()

