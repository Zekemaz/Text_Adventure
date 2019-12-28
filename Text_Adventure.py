import random
import time
import class_file
import function_file
# -----------FUNCTIONS--------
from class_file import Character
from function_file import createWorld, printas, print_loading

createWorld("The Town", 1, 1)

playerlist = []
player1=Character("Allegory", 100, 50, 50)
playerlist.append(player1)

enemylist = []
enemy1 = Character("xxx", 100, 50, 50)
#ennemylist.append(enemy1)

npclist = []


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
	drink = input("1. Cactus Juice ---- Enter [1]\n2. Beer         ---- Enter [2]\n3. Whiskey      ---- Enter [3]\n   ----> ")
	if int(drink) != 1:
		printas("barman", "Are you sure you want this ? Why don't you try something else ?")

printas("barman", "Well, good for you I don't know one drink better than this one !\
 But sadly you bought the last one. I know some people that will be angry knowing this.\n")
time.sleep(0.5)

sit = input("Do you want to stand at the bar or sit down at a table ? [Stand]/[Sit] \n").lower().strip()
while sit != "sit":
	printas("Story Teller", "Hm.. I'd say we sit what do you think ?\n")
	sit = input("Do you want to stand at the bar or sit down at a table ? [Stand]/[Sit] \n").lower().strip()

printas("Story Teller", "Allegory goes and sit alone sipping on his juice...\n\n")
time.sleep(1.5)

# -----------NPC INTERACTION--------
# -----------NPC INTERACTION--------
# -----------NPC INTERACTION--------
# -----------NPC INTERACTION--------
# -----------NPC INTERACTION--------
# -----------NPC INTERACTION--------
# -----------NPC INTERACTION--------
# -----------NPC INTERACTION--------
# -----------NPC INTERACTION--------

npc1 = Character("NPC-Julien", 1, 1, 1)
npclist.append(npc1)
print("*************POP*************\n\n")
printas("NPC", "Hey there, my name is Julien\n")
printas(player1.name, "Good morning, what can I do for you ?\n")
printas(npc1.name, "Well I heard you bought the last Cactus Juice of the town !? Yes I know... \
 News fly extremely fast ! It's normal have you seen how small this town is ? Anyway... Now that you bought the \
last juice you've gotta help us get some more.\n\n")

#------------------------MINI GAME------------------------
#------------------------MINI GAME------------------------
#------------------------MINI GAME------------------------
#------------------------MINI GAME------------------------


answer = "a"

while answer != "yes" and answer != "no":
	answer = input("[STORY TELLER] : Do we want to help them ? [Yes] / [No]\n   ----> ").lower().strip()

if answer == "no":
	printas(npc1.name, "What ? No !? How dare you ! You finish our stock and you dare say NO ?... You know what, \
we're going to play a game ! If I win you help the town, and if you win you don't have to.\n")
	print("The game is Who has the highest number ! It's simple you have to draw the highest number inside a deck of 10 cards !\n")

	score = 0
	while score >= 0:
		print_loading(npc1.name, "draws a card")
		pickAI = random.randint(4,10)
		time.sleep(0.5)
		printas(npc1.name,"I have got the %r. Your Turn now !" %(pickAI))
		time.sleep(0.5)
		print_loading(player1.name, "draws a card")
		pickPlayer = random.randint(1,10)
		time.sleep(0.5)
		printas(player1.name,"I have got the %r !" %(pickPlayer))
		score = pickPlayer - pickAI
		excuses = ["I had cold hands. We have to start again\n", "I sneezed so I closed my eyes, It doesn't count.\n", "You cheated !\n"]
		if score < 0:
			printas(npc1.name, "I won ! haha you've gotta help us now !\n")
		elif score > 0:
			printas(npc1.name, random.choice(excuses))
		elif score == 0:
			printas("Story Teller", " Egalité ! !\n")
elif answer == "yes":
    printas(npc1.name, "Oh how nice of you ! You'll redeem yourself once you replenish the reserve of Juice.\n")

		

