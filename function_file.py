import time
import sys

def createWorld(name, long, lat):
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
