import random
import time

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
# -----------INTRO--------
# -----------INTRO--------
# -----------INTRO--------
# -----------INTRO--------
# -----------INTRO--------
# -----------INTRO--------
# -----------INTRO--------
print("----------------------------------------------------------------")
print("In this adventure you'll play as Allegory, a magnificient Cowboy...")
print("----------------------------------------------------------------")



# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------

print("Allegory enters the bar in The Town to refresh himself with a drink.\n")
printas("barman", "Welcome in the CactusPub ! You can have anything to drink ! Make a choice")

drink = 0

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

# -----------PNJ INTERACTION--------
# -----------PNJ INTERACTION--------
# -----------PNJ INTERACTION--------
# -----------PNJ INTERACTION--------
# -----------PNJ INTERACTION--------
# -----------PNJ INTERACTION--------
# -----------PNJ INTERACTION--------
# -----------PNJ INTERACTION--------
# -----------PNJ INTERACTION--------

pnj1 = Character("PNJ-Julien", 1, 1, 1)
pnj.append(pnj1)
print("*************POP*************\n\n")
printas("pnj", "Hey there, my name is Julien\n")
printas(player1.name, "Good morning, what can I do for you ?\n")
printas(pnj1.name, "Well I heard you bought the last Cactus Juice of the town !? Yes I know... \
 News fly extremely fast ! It's normal have you seen how small this town is ? Anyway... Now that you bought the \
last juice you've gotta help us get some more.\n\n")

answer = "a"
while answer != "yes":
	answer = input("What do you say ? [Yes] / [No]\n").lower().strip()

	if answer == "no":
		printas(pnj1.name, "What ? No !? How dare you ! You finish our stock and you dare say NO ?... You know what, \
we're going to play a game ! If I win you help the town, and if you win you don't have to.\n")
		print("The game is Who has the highest number ! It's simple you have to draw the highest number inside a deck of 10 cards !\n")
		print(pnj1.name + " draws a card...")
		pickAI = random.randint(1,10)
		time.sleep(1)
		printas(pnj1.name, "I have got the %r. Your Turn now !" %(pickAI))
		print(player1.name + " draws a card...")
		pickPlayer = random.randint(1,10)
		time.sleep(1)
		printas(player1.name, "I have got the %r !" %(pickAI))
				
printas(pnj1.name, "Oh how nice of you ! You'll redeem yourself once you replenish the reserve of Juice.")
print("hvhhhgh")
