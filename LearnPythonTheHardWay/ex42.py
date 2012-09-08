#!/usr/bin/python
## Animal is-a object (yes, sort of confugsin) Look at the extra credit
class Animal(object):
	pass

## Dog is-a object
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name 
		self.name = name

## Cat is-a object
class Cat(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet
		self.pet = None

## Employee is-a object
class Employee(Person):

	def __init__(self, name, salary):
		## Calling the parent class constructor
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a object
class Salmon(Fish):
	pass

## Halibut is-a object
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()
