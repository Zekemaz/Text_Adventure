import time
import sys

def createWorld(name: str, long: int, lat: int):
	print("Welcome to", name, "your position is now", long,",",lat,"\n")


def printas(name: str, text:str):
    print("[" + name.upper() + "] : " + text)




def print_Loading_Name(name: str, text:str):
    print("[" + name.upper() + "] : " + text, end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(" ", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".")
    sys.stdout.flush()
    time.sleep(0.5)

def print_Loading(text:str):
    print(text, end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(" ", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".")
    sys.stdout.flush()
    time.sleep(0.5)

def print_Short_Loading(text:str):
    print(text, end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".")
    sys.stdout.flush()
    time.sleep(0.5)


def loadingbar(nbrsecond: int, timespeed: int = 1):
    for i in range(1, nbrsecond):
        if i %4 == 0:
            print(" ", end="")
            sys.stdout.flush()
        else:
            print(".", end="")
            sys.stdout.flush()
        time.sleep(1/timespeed)
        

def updateMoney(amount: int, blood_thorn):
    #déclarer resultat
    resultat = 0
    print("Blood Thorns : %r" % (blood_thorn))
    #Faire calcul
    resultat = blood_thorn + amount
    #Afficher resultat
    print("Blood Thorns : %r + %r " % (blood_thorn, amount))
    print_Short_Loading("")
    print("Blood Thorns : %r\n" % (resultat)) 
    return resultat
