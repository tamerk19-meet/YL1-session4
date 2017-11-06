class Animal(object):
	def __init__(self,sound,name,age,favourite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favourite_color = favourite_color
	def eat(self,food):
		print("Yummy!! "+ self.name + "is eating" + "food")
	def description(self):
		print(self.name + " is " + str(self.age) +" years old and loves the color "+ self.favourite_color)

Rani=Animal("nice things","Rani",11,'black')
Rani.eat("Grape Leaves")
Rani.description()
