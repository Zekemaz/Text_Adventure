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



player = []
player.append(Character("Allegory", 100, 50, 50))

ennemy = []
#ennemy.append(Character(Allegory, 100, 50, 50))

png = []
#png.append(Character(Julien, 1, 1, 1))

# -----------INTRO--------
print("----------------------------------------------------------------")
print("In this adventure you'll play as Allegory, a magnificient Cowboy...")
print("----------------------------------------------------------------")

print("Allegory enters the bar in The Town to refresh himself with a drink.")


# -----------CHOICE DRINk--------
drink = input("What drink would you like ?\n 1. Beer\n 2. Cactus Juice\n 3. Whiskey\n   ----> ")
while int(drink) < 1 or int(drink) > 3 :
	drink = input("What drink would you like ?\n 1. Beer\n 2. Cactus Juice\n 3. Whiskey\n   ----> ")

while int(drink) == 1:
	print("Are you sure you want a beer ? Why don't you try a Juice ?")
	#time.sleep(1)
	drink = input("What drink would you like ?\n 1. Beer\n 2. Cactus Juice\n 3. Whiskey\n   ----> ")

if int(drink) == 2:
	print("Yes ! Now that's what I'm talking about ! An excellent choice !")
	#time.sleep(1)
	print("As good a choice this was, you bought the last Cactus Juice... \
	Some people are going to get angry. Good Luck !")

while int(drink) == 3:
	print("Are you sure you want a whiskey ? Why don't you try a Juice ?")
	#time.sleep(1)
	drink = input("What drink would you like ?\n 1. Beer\n 2. Cactus Juice\n 3. Whiskey\n")

