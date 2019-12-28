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
