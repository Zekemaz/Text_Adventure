import random
import time
import class_file
import function_file
# -----------FUNCTIONS AND CLASSES--------
from class_file import Entity, Character, Player, Enemy, Item
from function_file import createWorld, printas, print_Loading_Name, print_Loading, print_Short_Loading, loadingbar, updateMoney

createWorld("The Town", 1, 1)
# -----------PLAYER, ENEMY, NPC LIST--------

playerlist = []
player1=Player("Allegory", 100, 50, 50)
playerlist.append(player1)

enemylist = []
enemy1 = Enemy("xxx", 100, 50, 50)
#ennemylist.append(enemy1)

npclist = []

# -----------ITEM LIST--------
itemlist = []

# -----------GAME MONEY--------
blood_thorn = 0



# -----------INTRO--------
# -----------INTRO--------
# -----------INTRO--------
# -----------INTRO--------
# -----------INTRO--------
# -----------INTRO--------
# -----------INTRO--------
# -----------INTRO--------
print("----------------------------------------------------------------")
print("In this adventure you'll play as Allegory, a magnificient Cowboy")
print("----------------------------------------------------------------")


loadingbar(5, 2)
print("\n")
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------

printas("story teller", "You enter the bar in The Town to refresh yourself with a drink.\n")
printas("barman", "Welcome in the CactusPub ! You can have anything to drink ! Make a choice")

drink = 0

while int(drink) != 1:
	print("The list of drinks")
	drink = input("1. Cactus Juice	---- Enter [1]\n2. Beer		---- Enter [2]\n3. Whiskey	---- Enter [3]\n   ----> ")
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

npc1 = Entity("NPC-Julien")
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

time.sleep(2)
answer = "a"

while answer != "yes" and answer != "no":
	answer = input("[STORY TELLER] : Do we want to help them ? [Yes] / [No]\n   ----> ").lower().strip()

if answer == "no":
	printas(npc1.name, "What ? No !? How dare you ! You finish our stock and you dare say NO ?... You know what, \
we're going to play a game ! If I win you help the town, and if you win you don't have to.\n")
	print("The game is Who has the highest number ! It's simple you have to draw the highest number inside a deck of 10 cards !\n")
	time.sleep(2)
	score = 0
	while score >= 0:
		print_Loading("NPC-Julien draws a card")
		pickAI = random.randint(4,10)
		time.sleep(0.5)
		printas(npc1.name,"I have got the %r. Your Turn now !" %(pickAI))
		time.sleep(0.5)
		print_Loading("You draw a card")
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

#------------------------GAME------------------------
#------------------------GAME------------------------
#------------------------GAME------------------------
#------------------------GAME------------------------
#------------------------GAME------------------------
#------------------------GAME------------------------
#------------------------GAME------------------------

printas(npc1.name, "Ok... it's basically the adventure of a lifetime. All you have to do is travel through the\
desert to get to the forest to get\
us some cactus juice. See how easy that sounds ?\n Now I'm going to give you this \
small ikea cherry wood faucet that you will need to shank into the juiciest and plumpiest cactus you'll find.\n\n")
time.sleep(3)

item1 = Item("Small Ikea Cherry Wood Faucet", "Tap/Robinet")
itemlist.append(item1)
time.sleep(2)

printas("story teller", "YOU OBTAINED A 'Small Ikea Cherry Wood Faucet' ! ! !\n")
printas("story teller", "Ok now that you have the faucet we can go outside and get you your ride.\n")
print_Loading_Name("story teller", "You head outside")

#------------------------GRAB MOUNT------------------------
#------------------------GRAB MOUNT------------------------
#------------------------GRAB MOUNT------------------------
#------------------------GRAB MOUNT------------------------
#------------------------GRAB MOUNT------------------------
#------------------------GRAB MOUNT------------------------

printas("story teller", "Go grab your ride and then we'll tune it.\n")
mount = 0
while int(mount) != 1:
	print("		The mounts in front of the pub : ")
	mount = input("1. Turtle Marianne	---- Enter [1]\n2. Spirit the Stallion	---- Enter [2]\n\
3. Roger Rabbit		---- Enter [3]\n4. Pig Rodolph		---- Enter [4]\n   ----> ")
	if int(mount) != 1:
		printas("story teller", "That's not your mount ? Stealing is bad ! !\n")

#------------------------SHOP FOR MOUNT------------------------
#------------------------SHOP FOR MOUNT------------------------
#------------------------SHOP FOR MOUNT------------------------
#------------------------SHOP FOR MOUNT------------------------
#------------------------SHOP FOR MOUNT------------------------
#------------------------SHOP FOR MOUNT------------------------

printas("story teller", "Ok. We're almost ready to leave town. First let's go to the shop.\n")
print_Loading(" ")
printas("story teller", "That's the shop right there. Let me give you 200 Blood Thorns so you can purchase something\n")
#------------------------MONEY INTRODUCTION------------------------
blood_thorn = updateMoney(200, blood_thorn)
time.sleep(1)

npc2 = Entity("NPC-Marchande")
npclist.append(npc2)

printas(npc2.name, "Hello you ! What are you looking for today ?\n")
choice = 0
while int(choice) != 1:
	print("			Shop List : ")
	choice = input("150 BT. Unbridled Chrome Exhaust	---- Enter [1]\n200 BT. Gold Shell			---- Enter [2]\n\
210 BT. Spiky Rims			---- Enter [3]\n400 BT. Carbon Helmet			---- Enter [4]\n   ----> ")
	if int(choice) != 1:
		printas("story teller", "You don't need this yet...")

printas(npc2.name, "Here, give me the money and I'll fit it onto your turtle.\n")

blood_thorn = updateMoney(-150, blood_thorn)

