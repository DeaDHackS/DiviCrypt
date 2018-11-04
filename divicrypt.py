#!/usr/bin/env python
import optparse
from colorama import Style, Fore
import os
import sys
import py_compile
import datetime
import random
import shutil
import inspect

parser = optparse.OptionParser()

parser.add_option('-f', '--file',
    action="store", dest="file",
    help="File to compile or obfuscate|Encrypt", default="")
parser.add_option('-m', '--mode',
    action="store", dest="mode",
    help="Mode to use (compile / obfuscate|Encrypt / encode)", default="")

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

Raw_Data = datetime.datetime.now()
currentDate = str(Raw_Data)

#os.system("cls")
os.system("clear")

check_file_back = os.getcwd()+"/script_backup/"+options.file
if os.path.exists(check_file_back):
    os.remove(check_file_back)

print color.BLUE + color.BOLD + """
 _______   __  ____    ____  __    ______ .______     ____    ____ .______   .___________.
|       \ |  | \   \  /   / |  |  /      ||   _  \    \   \  /   / |   _  \  |           |
|  .--.  ||  |  \   \/   /  |  | |  ,----'|  |_)  |    \   \/   /  |  |_)  | `---|  |----`
|  |  |  ||  |   \      /   |  | |  |     |      /      \_    _/   |   ___/      |  |     
|  '--'  ||  |    \    /    |  | |  `----.|  |\  \----.   |  |     |  |          |  |     
|_______/ |__|     \__/     |__|  \______|| _| `._____|   |__|     | _|          |__|     
(+) Python Backdoor Framework (-) Coded By Ghosty / DeaDHackS Team (+)     
(+) https://www.github.com/DeaDHackS/ (+)
(+) Version 1.0 (+)
"""

print color.BLUE + "[SESSION STARTED]" + color.END + " At " + currentDate + "\n\n"

if not options.mode:
    print color.RED + "(-)" + color.END + " Error Mode is not set! See --help / -h for more informations" 
    print color.RED + "[SESSION STOPPED]" + color.END + " At " + currentDate + "\n\n"
    sys.exit()
elif options.mode == "Obfuscate" or options.mode == "obfuscate":
    mode = "Obfuscate"
    print color.GREEN + "(+)" + color.END + " Mode => Obfuscate"

elif options.mode == "Compile" or options.mode == "compile":
    mode = "Compile"
    print color.GREEN + "(+)" + color.END + " Mode => Compile" 

elif options.mode == "Encode" or options.mode == "encode":
    mode = "Encode"
    print color.GREEN + "(+)" + color.END + " Mode => Encode"   
    
else:
    print color.RED + "(-)" + color.END + " Error selected mode is not recognised See --help / -h for more informations"  
    print color.RED + "[SESSION STOPPED]" + color.END + " At " + currentDate + "\n\n"
    sys.exit() 

if not options.file:
    print color.RED + "(-)" + color.END + " Error file is not set! See --help / -h for more informations"
    print color.RED + "[SESSION STOPPED]" + color.END + " At " + currentDate + "\n\n"
    sys.exit()
else:
    print color.GREEN + "(+)" + color.END + " Script To " + mode + " => " + options.file
    if not os.path.exists(options.file):
       print color.RED + "(-)" + color.END + " Error Selected File does not seem to exist! Make sure file is accessable and exists!" 
       print color.RED + "[SESSION STOPPED]" + color.END + " At " + currentDate + "\n\n"
       sys.exit()

if mode == "Obfuscate":
    shutil.copy(options.file, "script_backup")
    print color.GREEN + "\n(+)" + color.END + " Backup saved in scripts_backup in case.."
    print color.YELLOW + "(i)" + color.END + " Reading " + options.file + "..."
    ext = os.path.splitext(options.file)[-1].lower()
    if ext == ".py" or ext == ".pyc" or ext == ".pyz":
      print color.GREEN + "(+)" + color.END + " File format seems to be Python!.."
    else:
      print color.RED + "(-)" + color.END + " File format seems to not be Python!.."
      print color.RED + "[SESSION STOPPED]" + color.END + " At " + currentDate + "\n\n"
      sys.exit()
    print color.YELLOW + "(i)" + color.END + " Prepraring Obfuscation, please stand by while DiviCrypt is doing the job!"
    print color.BLUE + "\n(>    Obfuscation Zone    <)" + color.END
    print color.YELLOW + "(i)" + color.END + " Calling Junk Code Script ...(will not effect the size of the script)"
    os.system("python insert_junk_code.py --file="+options.file)
    print color.GREEN + "(+)" + color.END + " Finished Writting Junk Code ..."
    print color.YELLOW + "(i)" + color.END + " Obfuscating(encrypting) File => " + options.file + "... 1... 2... 3"
    os.system("python obfuscate_code.py --file="+options.file)
    print color.GREEN + "(+)" + color.END + " Done! Have fun! Thanks for using DiviCrypt"
elif mode == "Compile":
    shutil.copy(options.file, "script_backup")
    print color.GREEN + "\n(+)" + color.END + " Backup saved in scripts_backup in case.."
    print color.YELLOW + "(i)" + color.END + " Reading " + options.file + "..."
    ext = os.path.splitext(options.file)[-1].lower()
    if ext == ".py" or ext == ".pyc" or ext == ".pyz":
      print color.GREEN + "(+)" + color.END + " File format seems to be Python!.."
    else:
      print color.RED + "(-)" + color.END + " File format seems to not be Python!.."
      print color.RED + "[SESSION STOPPED]" + color.END + " At " + currentDate + "\n\n"
      sys.exit()
    print color.YELLOW + "(i)" + color.END + " Prepraring Compiling, please stand by while DiviCrypt is doing the job!"
    print color.BLUE + "\n(>    Obfuscation Zone    <)" + color.END
    print color.YELLOW + "(i)" + color.END + " Calling Junk Code Script ...(will not effect the size of the script)"
    os.system("python insert_junk_code.py --file="+options.file)
    print color.GREEN + "(+)" + color.END + " Finished Writting Junk Code ..."
    print color.YELLOW + "(i)" + color.END + " Compiling File => " + options.file + "... 1... 2... 3"
    os.system("python compiler.py --file="+options.file)
    print color.GREEN + "(+)" + color.END + " Done! Have fun! Thanks for using DiviCrypt"


elif mode == "Encode":
    shutil.copy(options.file, "script_backup")
    print color.GREEN + "\n(+)" + color.END + " Backup saved in scripts_backup in case.."
    print color.YELLOW + "(i)" + color.END + " Reading " + options.file + "..."
    ext = os.path.splitext(options.file)[-1].lower()
    if ext == ".py" or ext == ".pyc" or ext == ".pyz":
      print color.GREEN + "(+)" + color.END + " File format seems to be Python!.."
    else:
      print color.RED + "(-)" + color.END + " File format seems to not be Python!.."
      print color.RED + "[SESSION STOPPED]" + color.END + " At " + currentDate + "\n\n"
      sys.exit()
    print color.YELLOW + "(i)" + color.END + " Prepraring Encoding, please stand by while DiviCrypt is doing the job!"
    print color.BLUE + "\n(>    Encoding Zone    <)" + color.END
    print color.YELLOW + "(i)" + color.END + " Calling Base64 Encode Script ..."
    os.system("python base64_encoder.py --file="+options.file)
    print color.GREEN + "(+)" + color.END + " Done! Have fun! Thanks for using DiviCrypt"
