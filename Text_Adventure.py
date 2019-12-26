import random
import time
from pprint import pprint

# -----------FUNCTIONS--------
def createWorld(name, long, lat):
	print("Welcome to", name, "your position is now", long,",",lat,"\n")

createWorld( "The Town", 1, 1)

class Character:
	def __init__(self, name, health, attack, defence):
		self.name = name
		self.health = health
		self.attack = attack
		self.defence = defence

	def getName(self):
		return self.name
	def getHealth(self):
		return self.health
	def getAttack(self):
		return self.attack
	def getDefence(self):
		return self.defence

	def setName(self, newName):
		self.name = newName
	def setHealth(self, newHealth):
		self.health = newHealth
	def setAttack(self, newAttack):
		self.attack = newAttack	
	def setDefence(self, newDefence):
		self.defence = newDefence	


def printas(name: str, text:str):
    print("[" + name.upper() + "] : " + text)


player = []

player1=Character("Allegory", 100, 50, 50)

player.append(player1)

enemy = []
enemy1 = Character("xxx", 100, 50, 50)
#ennemy.append(enemy1)

pnj = []


# -----------INTRO--------
print("----------------------------------------------------------------")
print("In this adventure you'll play as Allegory, a magnificient Cowboy...")
print("----------------------------------------------------------------")



# -----------CHOICE DRINk--------
print("Allegory enters the bar in The Town to refresh himself with a drink.\n")
printas("barman", "Welcome in the CactusPub ! You can have anything to drink ! Make a choice")

drink = 0

#drink = input("What drink would you like ?\n 1. Cactus Juice\n 2. Beer\n 3. Whiskey\n   ----> ")
while int(drink) != 1:
	print("The list of drinks")
	drink = input("1. Cactus Juice\n2. Beer\n3. Whiskey\n   ----> ")
	if int(drink) != 1:
		print("Are you sure you want this ? Why don't you try something else ?")

printas("barman", "Well, good for you I don't know one drink better than this one !\
 But sadly you bought the last one. I know some people that will be angry knowing this.\n")
time.sleep(0.5)

sit = input("Do you want stand at the bar or sit down at a table ? [Stand]/[Sit] \n").lower().strip()
while sit != "sit":
	print("Hm.. I'd say we sit what do you think ?\n")
	sit = input("Do you want stand at the bar or sit down at a table ? [Stand]/[Sit] \n").lower().strip()

print("Allegory goes and sit alone sipping on his juice...\n\n")
time.sleep(1.5)

# -----------PNJ COMES--------

pnj1 = Character("PNJ-Julien", 1, 1, 1)
pnj.append(pnj1)
print("*************POP*************\n\n")
printas("pnj", "Hey there, my name is Julien\n")
printas(player1.name, "Good morning, what can I do for you ?\n")
printas(pnj1.name, "Well I heard you bought the last Cactus Juice of the town !? Yes I know... \
 News fly extremely fast ! Have you seen how small this town is ?\nAnyway. Now that you bought the \
 last juice you've gotta help us get some more. What do you say ?" )