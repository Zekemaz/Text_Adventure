class Entity:
	def __init__(self, _name):
		self.name = _name

	def getName(self):
		return self.name
	
	def setName(self, _newName):
		self.name = _newName


class Character(Entity):
	def __init__(self, _name, _health, _attack, _defence):
		super().__init__(_name)
		self.health = _health
		self.attack = _attack
		self.defence = _defence
	

	def getHealth(self):
		return self.health
	def getAttack(self):
		return self.attack
	def getDefence(self):
		return self.defence

	def setHealth(self, _newHealth):
		self.health = _newHealth
	def setAttack(self, _newAttack):
		self.attack = _newAttack	
	def setDefence(self, _newDefence):
		self.defence = _newDefence	


class Player(Character):
	def __init__(self, _name, _health, _attack, _defence):
		super().__init__(_name, _health, _attack, _defence)


class Enemy(Character):
	def __init__(self, _name, _health, _attack, _defence):
		super().__init__(_name, _health, _attack, _defence)



class Item:
	def __init__(self, _name, _utility):
		self.name = _name
		self.utility = _utility