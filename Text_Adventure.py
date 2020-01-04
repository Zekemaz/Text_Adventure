import random
import time

import class_file
import function_file
# -----------FUNCTIONS AND CLASSES--------
from class_file import Character, Enemy, Entity, Item, Player, World
from function_file import (loadingbar, print_Loading, print_Loading_Name,
                           print_Short_Loading, printas, updateMoney)

# -----------WORLD LIST--------
worldlist = []

# -----------PLAYER LIST--------

playerlist = []
player1=Player("Allegory", 100, 50, 50)
playerlist.append(player1)

# -----------ENEMY LIST--------

enemylist = []

# -----------NPC LIST--------

npclist = []
npc1 = Entity("STORY TELLER")
npclist.append(npc1)

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

# -----------THE TOWN--------
# -----------THE TOWN--------
# -----------THE TOWN--------
# -----------THE TOWN--------
# -----------THE TOWN--------
# -----------THE TOWN--------
# -----------THE TOWN--------
# -----------THE TOWN--------
# -----------THE TOWN--------
# -----------THE TOWN--------
world_1 = World("The Town", 1, 1) # --------- CREATION 1ST WORLD -------------
worldlist.append(world_1)

# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
# -----------CHOICE DRINk--------
npc2 = Entity("NPC-BARMAN") # --------- CREATION NPC 2 ---------
npclist.append(npc2)

printas(npc1.name, "You enter the bar in The Town to refresh yourself with a drink.\n")
printas(npc2.name, "Welcome in the CactusPub ! You can have anything to drink ! Make a choice")

drink = 0

while int(drink) != 1:
	print("The list of drinks")
	drink = input("1. Cactus Juice	---- Enter [1]\n2. Beer		---- Enter [2]\n3. Whiskey	---- Enter [3]\n   ----> ")
	if int(drink) != 1:
		printas(npc2.name, "Are you sure you want this ? Why don't you try something else ?")

printas(npc2.name, "Well, good for you I don't know one drink better than this one !\
 But sadly you bought the last one. I know some people that will be angry knowing this.\n")
time.sleep(0.5)

sit = input("Do you want to stand at the bar or sit down at a table ? [Stand]/[Sit] \n").lower().strip()
while sit != "sit":
	printas(npc1.name, "Hm.. I'd say we sit what do you think ?\n")
	sit = input("Do you want to stand at the bar or sit down at a table ? [Stand]/[Sit] \n").lower().strip()

printas(npc1.name, "Allegory goes and sit alone sipping on his juice...\n\n")
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

npc3 = Entity("NPC-Julien") # --------- CREATION NPC 3 ---------
npclist.append(npc3)

print("*************POP*************\n\n")
printas("NPC", "Hey there, my name is Julien\n")
printas(player1.name, "Good morning, what can I do for you ?\n")
printas(npc3.name, "Well I heard you bought the last Cactus Juice of the town !? Yes I know... \
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
	printas(npc3.name, "What ? No !? How dare you ! You finish our stock and you dare say NO ?... You know what, \
we're going to play a game ! If I win you help the town, and if you win you don't have to.\n")
	print("The game is Who has the highest number ! It's simple you have to draw the highest number inside a deck of 10 cards !\n")
	time.sleep(2)
	score = 0
	while score >= 0:
		print_Loading("NPC-Julien draws a card")
		pickAI = random.randint(4,10)
		time.sleep(0.5)
		printas(npc3.name,"I have got the %r. Your Turn now !" %(pickAI))
		time.sleep(0.5)
		print_Loading("You draw a card")
		pickPlayer = random.randint(1,10)
		time.sleep(0.5)
		printas(player1.name,"I have got the %r !" %(pickPlayer))
		score = pickPlayer - pickAI
		excuses = ["I had cold hands. We have to start again\n", "I sneezed so I closed my eyes, It doesn't count.\n", "You cheated !\n"]
		if score < 0:
			printas(npc3.name, "I won ! haha you've gotta help us now !\n")
		elif score > 0:
			printas(npc3.name, random.choice(excuses))
		elif score == 0:
			printas(npc1.name, " Egalité ! !\n")
elif answer == "yes":
    printas(npc3.name, "Oh how nice of you ! You'll redeem yourself once you replenish the reserve of Juice.\n")

#------------------------GAME------------------------
#------------------------GAME------------------------
#------------------------GAME------------------------
#------------------------GAME------------------------
#------------------------GAME------------------------
#------------------------GAME------------------------
#------------------------GAME------------------------

printas(npc3.name, "Ok... it's basically the adventure of a lifetime. All you have to do is travel through the \
desert to get to the forest to get us some cactus juice. See how easy that sounds ?\n \
Now I'm going to give you this small ikea cherry wood faucet that you will need to \
shank into the juiciest, plumpiest and beautifulest cactus you'll find.\n\n")
time.sleep(3)

item1 = Item("Small Ikea Cherry Wood Faucet", "Tap/Robinet")
itemlist.append(item1)
time.sleep(2)

printas(npc1.name, "YOU OBTAINED A 'Small Ikea Cherry Wood Faucet' ! ! !\n")
printas(npc1.name, "Ok now that you have the faucet we can go outside and get you your ride.\n")
print_Loading_Name(npc1.name, "You head outside")

#------------------------GRAB MOUNT------------------------
#------------------------GRAB MOUNT------------------------
#------------------------GRAB MOUNT------------------------
#------------------------GRAB MOUNT------------------------
#------------------------GRAB MOUNT------------------------
#------------------------GRAB MOUNT------------------------

printas(npc1.name, "Go grab your ride and then we'll tune it.\n")
mount = 0
while int(mount) != 1:
	print("		The mounts in front of the pub : ")
	mount = input("1. Turtle Marianne	---- Enter [1]\n2. Spirit the Stallion	---- Enter [2]\n\
3. Roger Rabbit		---- Enter [3]\n4. Pig Rodolph		---- Enter [4]\n   ----> ")
	if int(mount) != 1:
		printas(npc1.name, "That's not your mount ? Stealing is bad ! !\n")

#------------------------SHOP FOR MOUNT------------------------
#------------------------SHOP FOR MOUNT------------------------
#------------------------SHOP FOR MOUNT------------------------
#------------------------SHOP FOR MOUNT------------------------
#------------------------SHOP FOR MOUNT------------------------
#------------------------SHOP FOR MOUNT------------------------

printas(npc1.name, "Ok. We're almost ready to leave town. First let's go to the shop.\n")
print_Loading(" ")
printas(npc1.name, "That's the shop right there. Let me give you 200 Blood Thorns so you can purchase something\n")
#------------------------MONEY INTRODUCTION------------------------
blood_thorn = updateMoney(200, blood_thorn)
time.sleep(1)

npc4 = Entity("NPC-Shop Worker") # --------- CREATION NPC 4 ---------
npclist.append(npc4)

printas(npc4.name, "Hello you ! What are you looking for today ?\n")
choice = 0
while int(choice) != 1:
	print("			Shop List : ")
	choice = input("150 BT. Unbridled Chrome Exhaust	(Speed +10)	---- Enter [1]\n200 BT. Gold Shell			(Armor +20)	---- Enter [2]\n\
210 BT. Spiky Rims			(Attack +5)	---- Enter [3]\n400 BT. Carbon Helmet			(Armor +5)	---- Enter [4]\n   ----> ")
	if int(choice) != 1:
		printas(npc1.name, "You don't need this yet...")

printas(npc4.name, "Here, give me the money and I'll fit it onto your turtle.\n")

blood_thorn = updateMoney(-150, blood_thorn)

time.sleep(0.5)

item2 = Item("Unbridled Chrome Exhaust", "Speed +10")
itemlist.append(item2)
time.sleep(1)

printas(npc1.name, "YOU OBTAINED A 'Unbridled Chrome Exhaust' ! ! !\n")

print("* Mechanic sound * CLICK CLACK BLOOM BAM BIM\n")
loadingbar(5,2)
print("\n")
printas(npc4.name, "That's it, I'm done. Your turtle is ready.\n\n")
printas(npc1.name, "Let's goooooo !")
loadingbar(5, 2)
print("\n")

# -----------FOREST--------
# -----------FOREST--------
# -----------FOREST--------
# -----------FOREST--------
# -----------FOREST--------
# -----------FOREST--------
# -----------FOREST--------
# -----------FOREST--------
world_2 = World("The Cactus Forest", 1, 2) # --------- CREATION 2ND WORLD ---------
worldlist.append(world_2)


printas(npc1.name, "10 km/h, wind in the hair, speeding like never before you finally arrive in The Cactus Forest")
loadingbar(5,2)
print("\n")

printas(npc1.name, "As you can see, this place is filled with cactus. Remember which one does NPC-Julien want\n")

#describe campus
printas(player1.name, "There's so many cactus ! I will have to use my common sense to find the one !\n")
choiceCactus = 0
while int(choiceCactus) != 3:
	choiceCactus = input("[STORY TELLER] : \nOn the left you can see this small Cactus ! He seems really beautiful \
but I don't think he will give us enough juice though...   Enter [1]\n\nBehind you there is this massive cactus, \
he's not beautiful but I'm pretty sure we will get enough juice from his big size.      Enter [2]\n\nJust ahead \
of you there is this young cactus. He looks rather plumpy, juicy and I wouldn't say he's ugly.                  \
      Enter [3]\n\nOn your right we both can see the most beautiful cactus ! But I reckon it's just a female who \
put on a lot of make up.           Enter [4]\n\n")
	if int(choiceCactus) != 3:
		printas(npc1.name, "I'm really not sure about this...\n")

printas(npc1.name, "Yes ! ! I also think that this is the one !\n")


enemy1 = Enemy("Campus The Cactus", 100, 50, 50) # --------- CREATION ENEMY ---------
enemylist.append(enemy1)

#faire connaissance avec lui (choix de questions)
printas(npc1.name, "Hey you ! What's your name ?!\n")
printas("[ ??? ] : ", " Hmm my name is Campus the Cactus ! what can I do for you ?\n")
printas(npc1.name, "Ask him questions !\n")

choiceQuestion = 0
while int(choiceQuestion) != 1 and int(choiceQuestion) != 2 and int(choiceQuestion) != 3:
	choiceQuestion = input("[STORY TELLER] : Randomly choose questions from [1] to [3].\n	----->")
	if int(choiceQuestion) != 1 and int(choiceQuestion) != 2 and int(choiceQuestion) != 3:
		printas(player1.name, "It's question [1] to [3]. So you have to enter the corresponding number ! I hate repeting myslef !\n")
	if int(choiceQuestion) == 1:
		printas(player1.name, "Well you look like a friendly Cactus, can I ask you something ?\n")
		printas(enemy1.name, "Oh thank you there, how can I help you !\n")
		printas(player1.name, " Well I'm coming from " + world_1.name + " and we have a problem regarding our supply of Cactus Juice so I was \
wondering if we could find a friendly way, that would benefit both " + world_1.name + " and " + world_2.name +", to replenish our stock... \
I know it sounds weird but I'm sure there's something you'd like that we can provide for you...\n")
		printas(enemy1.name, "rhouu tsoöme ngootörou use'as e'aı doödoö bɨre'a uhr bɨngoörindo bɨ’aashii... rödiwitö.\n")
	if int(choiceQuestion) == 2:
		printas(player1.name, "Hm... You look quite juicy I think I'll stab ya !\n")
		printas(enemy1.name, "rhouu tsoöme ngootörou use'as e'aı doödoö bɨre'a uhr bɨngoörindo bɨ’aashii... rödiwitö.\n")
	if int(choiceQuestion) == 3:
		printas(player1.name, "Would you be willing to come to " + world_1.name + " with me so I can replenish the Cactus Juice reserve ?\n")
		printas(enemy1.name, "rhouu tsoöme ngootörou use'as e'aı doödoö bɨre'a uhr bɨngoörindo bɨ’aashii... rödiwitö.\n")

#des cactus arrivent par derriere? ou le vent ?
printas(player1.name, "Hmm... What ?")
printas(npc1.name, "I think he was talking to the other ones and I don't think it's a good sign ! Look around ! I think all the cactus are \
coming around to attack us\n")
printas(player1.name, "Or Maybe it's the wind ? DUH...\n")
time.sleep(1)
loadingbar(5,2)
printas(enemy1.name, "Laklac Ÿokani forteë aomagho\n")



# coup de pression/coup destoc/ca jute

#jeanmarie l'épine attaque, petit jeu de défense. Jean marie gagne

#make fonction attack/def/loose hp in classes
#
#
#