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
print(colored("                                                                                                   ", "cyan"))
print(colored("                           ▄█       ▄██   ▄   ████████▄   ▄█     ▄████████                         ", "cyan"))
print(colored("                          ███       ███   ██▄ ███   ▀███ ███    ███    ███                         ", "cyan"))
print(colored("                          ███       ███▄▄▄███ ███    ███ ███▌   ███    ███                         ", "cyan"))
print(colored("                          ███       ▀▀▀▀▀▀███ ███    ███ ███▌   ███    ███                         ", "cyan"))
print(colored("                          ███       ▄██   ███ ███    ███ ███▌ ▀███████████                         ", "cyan"))
print(colored("                          ███       ███   ███ ███    ███ ███    ███    ███                         ", "cyan"))
print(colored("                          ███▌    ▄ ███   ███ ███   ▄███ ███    ███    ███                         ", "cyan"))
print(colored("                          █████▄▄██  ▀█████▀  ████████▀  █▀     ███    █▀                          ", "cyan"))
print(colored("                          ▀                                                                        ", "cyan"))
print(colored("  _______ __                          __                     __        __               __         ", "red"))
print(colored(" |       |  |--.-----.   .---.-.--.--|  |_.-----.-----.-----|  |--.   |  |--.----.--.--|  |_.-----.", "red"))
print(colored(" |.|   | |     |  -__|   |  _  |  |  |   _|  _  |__ --|__ --|     |   |  _  |   _|  |  |   _|  -__|", "red"))
print(colored(" `-|.  |-|__|__|_____|   |___._|_____|____|_____|_____|_____|__|__|   |_____|__| |_____|____|_____|", "red"))
print(colored("   |:  |                                                                                           ", "red"))
print(colored("   |::.|                                                                                           ", "red"))
print(colored("   `---'                                                                                           ", "red"))
print("===================================================================================================")
print("=                     Made Sten (Gespel) Heimbrodt [@Sten_Heimbrodt]                              =")
print("===================================================================================================")

args = parser.parse_args()
verbose = args.verb





def print_help():
    pass

def parseCommand(command, passlistpath, logfilepath):
    basecommand = command[0]
    if basecommand == "go":
        s = LydiaScanner(True, passlistpath, logfilepath, True)
        s.go(32)
    elif basecommand == "scan":
        s = LydiaScanner(True, passlistpath, logfilepath, False)
        s.go(32)


    elif basecommand == "exit":
        print(colored("Bye Bye :)", "cyan"))
        exit()
    else:
        print(colored("Unknown command!", "red"))


def menuLoop():
    while True:
        print(colored("lydia> ", "green"), end="")
        inarr = input().split(" ")
        current_date = datetime.now().strftime("%Y-%m-%d")
        logfile_name = f"logfile_{current_date}.txt"
        parseCommand(inarr, "rockyoufirst.txt", logfile_name)


if args.pwlist is None and args.logfile is None and args.threadcount is None:
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





