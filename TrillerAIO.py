import requests, os, colorama, random, string, threading, json,time
from time import sleep
from os import system
from colorama import Fore, Style
colorama.init()

system('mode con: cols=65 lines=20')
system("title " + "Made By FGLX")


def logo():
    msg = Fore.LIGHTMAGENTA_EX+"""
___________      .__.__  .__                
\__    ___/______|__|  | |  |   ___________ 
  |    |  \_  __ \  |  | |  | _/ __ \_  __ 
  |    |   |  | \/  |  |_|  |_\  ___/|  | \/
  |____|   |__|  |__|____/____/\___  >__|   
                                   \/
                                   """
    print(msg)
    print(Fore.WHITE+"$>"+Fore.LIGHTMAGENTA_EX+"Made By FGLX.sql#9999")
    print("")

def menu():
    print(Fore.WHITE+"$>1 | "+Fore.LIGHTMAGENTA_EX+"Username Checker")
    print(Fore.WHITE+"$>2 | "+Fore.LIGHTMAGENTA_EX+"View bot")
    print("")

video = ""
proxtxt = ""
timeouttime = 0
threads = 0

def Viewbot():
    os.system("cls")
    logo()
    print(Fore.WHITE+"$>"+Fore.LIGHTMAGENTA_EX+"Views are being sent")
    print(Fore.WHITE+"$>"+Fore.LIGHTMAGENTA_EX+"You will be put back to home when its over")
    sleep(3)
    os.system("cls")
    logo()
    with open(proxtxt) as f:
            for line in f:
                prox = line.strip("\n")
                proxy = {
                    'https' : f'http://{prox}'
                }
                try:
                    requests.get(f"{video}", proxies=proxy, timeout=timeouttime)
                except:
                    pass
    menuT()

def username():
     os.system("cls")
     logo()
     print(Fore.WHITE+"$>"+Fore.LIGHTMAGENTA_EX+"Usernames must be over 6!")
     usernametxt = input(Fore.WHITE+"?>"+Fore.LIGHTMAGENTA_EX+"Username txt:")
     os.system("cls")
     logo()
     with open(usernametxt) as f:
            for line in f:
                user = line.strip("\n")
                r = requests.get(f"https://social.triller.co/v1.5/api/users/by_username/{user}")
                if r.status_code == 200:
                    print(Fore.WHITE+"$>"+Fore.RED+f"{user}")
                else:
                    print(Fore.WHITE+"$>"+Fore.GREEN+f"{user}")
                    with open("Good Username.txt", "a+") as (k):
                        k.writelines(f"{user}\n")
                    pass
     menuT()

    
def menuT():
    global video 
    global proxtxt 
    global timeouttime 
    global threads
    os.system("cls")
    logo()
    menu()
    option = int(input(Fore.WHITE+"?>"+Fore.LIGHTMAGENTA_EX+""))
    while option != 0:
        if option == 1:
            os.system("cls")
            logo()
            username()
        elif option == 2:
            os.system("cls")
            logo()
            video = input(Fore.WHITE+"?>"+Fore.LIGHTMAGENTA_EX+"Video Link: ")
            proxtxt = input(Fore.WHITE+"?>"+Fore.LIGHTMAGENTA_EX+"Proxies: ")
            timeouttime = int(input(Fore.WHITE+"?>"+Fore.LIGHTMAGENTA_EX+"Timeout: "))
            threads = int(input(Fore.WHITE+"?>"+Fore.LIGHTMAGENTA_EX+"Threads: "))
            sleep(5)
            for x in range(threads):
                x = threading.Thread(target=Viewbot)
                x.start()
            sleep(5)
        else:
            pass


menuT()
