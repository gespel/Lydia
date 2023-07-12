#!/usr/bin/env python
from tabnanny import verbose
from termcolor import colored
from argparse import ArgumentParser
from core.scanner import LydiaScanner
from datetime import datetime

parser = ArgumentParser()
parser.add_argument("-p", "--passwordlist", dest="pwlist",
                    help="Path to the passwordlist")
parser.add_argument("-l", "--logfile", dest="logfile",
                    help="Path to logfile")
parser.add_argument("-q", "--quiet", dest="verb",
                    action="store_false", default=True,
                    help="don't print status messages to stdout")
parser.add_argument("-g", "--gui", dest="gui", action="store_true", default=False, help="start gui")
parser.add_argument("-t", "--threads", dest="threadcount",
                    help="Number of threads to work with")
print("                                                                                                   ")
print("                           ▄█       ▄██   ▄   ████████▄   ▄█     ▄████████                         ")
print("                          ███       ███   ██▄ ███   ▀███ ███    ███    ███                         ")
print("                          ███       ███▄▄▄███ ███    ███ ███▌   ███    ███                         ")
print("                          ███       ▀▀▀▀▀▀███ ███    ███ ███▌   ███    ███                         ")
print("                          ███       ▄██   ███ ███    ███ ███▌ ▀███████████                         ")
print("                          ███       ███   ███ ███    ███ ███    ███    ███                         ")
print("                          ███▌    ▄ ███   ███ ███   ▄███ ███    ███    ███                         ")
print("                          █████▄▄██  ▀█████▀  ████████▀  █▀     ███    █▀                          ")
print("                          ▀                                                                        ")
print("  _______ __                          __                     __        __               __         ")
print(" |       |  |--.-----.   .---.-.--.--|  |_.-----.-----.-----|  |--.   |  |--.----.--.--|  |_.-----.")
print(" |.|   | |     |  -__|   |  _  |  |  |   _|  _  |__ --|__ --|     |   |  _  |   _|  |  |   _|  -__|")
print(" `-|.  |-|__|__|_____|   |___._|_____|____|_____|_____|_____|__|__|   |_____|__| |_____|____|_____|")
print("   |:  |                                                                                           ")
print("   |::.|                                                                                           ")
print("   `---'                                                                                           ")
print("===================================================================================================")
print("=                     Made Sten (Gespel) Heimbrodt [@Sten_Heimbrodt]                              =")
print("===================================================================================================")

args = parser.parse_args()
verbose = args.verb







def parseCommand(command, passlistpath, logfilepath):
    basecommand = command[0]
    if basecommand == "go":
        s = LydiaScanner(True, passlistpath, logfilepath)
        s.go(32)


def menuLoop():
    while True:
        print(colored("lydia> ", "green"), end="")
        inarr = input().split(" ")
        current_date = datetime.now().strftime("%Y-%m-%d")
        logfile_name = f"logfile_{current_date}.txt"
        parseCommand(inarr, "rockyoufirst.txt", logfile_name)


if (args.pwlist == None and args.logfile == None and args.threadcount == None):
    menuLoop()

if (args.pwlist == None):
    print("No passwordlist defined!")
    exit()
passlistpath = args.pwlist
if (args.logfile == None):
    print("No logfilepath defined. Using default logs.txt")
    logfilepath = "log.txt"
else:
    logfilepath = args.logfile
if (args.threadcount == None):
    print("No threadcount given. Defaulting to 4 threads...")
    threads = 4
else:
    threads = int(args.threadcount)





