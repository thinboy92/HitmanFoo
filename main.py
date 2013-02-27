### Animal is-a object (yes, sort of confusing) look at the extra credit
class animal(object):

	def __init__(self, type):
		self.type = type 

	def fly(self):
		print "This %s can fly" %(self.type) 
		

## Dog is-a animal
class Dog(animal):
	
	def __init__(self, name):
		# class Doh has-a __init__ that accepts self and name parameters
		## Dog has-a name
		self.name = name

## cat is-a animal
class Cat(animal):

	def __init__(self, name):
		## class Cat has-a __init__ that accepts self and name parameters
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## class Person has-a __init__ that accepts self and name parameters
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):
	
	def __init__(self, name, salary):
		super(Employee, self).__init__(name) ## this
		## gives access to the name attribute
		## of Employee's parent object i.e. Person.
		## apparently useful in the case of multiple inheritance.
		## Employee has-a salary 
		self.name = name
		self.salary = salary
		print "%s's salary is %d" % (self.name,self.salary)

	def write(self,name,salary):
		print "This is invoked by using function in a class. %s's salary is %d" % (name,salary)

## Fish is-a object
class Fish(object):

	def __init__(self,steam):
		self.steam = steam()

	def fry():
		print "Whether to steam or fry %s" %(self.steam)

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat 
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## From mary, take the attribute pet and set it to variable satan. 
mary.pet = satan # Now, mary's pet is-a cat object named satan
				 

## frank is-a Employee with parameters Frank and 120000
frank = Employee("Frank", 120000)
frank.write("Frank", 120000)

## from frank, take the pet attribute and set it to rover. 
frank.pet = rover # frank's pet is-a dog object named rover

## set flipper to an instance of class Fish
# flipper is-a fish
#flipper = Fish(steam)
##afeez, When I run it in python or Terminal this is what I get:
##Traceback (most recent call last):
##  File "ex42.py", line 85, in <module>
##    flipper = Fish()
##TypeError: __init__() takes exactly 2 arguments (1 given)


## setting crouse to an instance of class Salmon
# course is-a salmon and salmon is-a fish
#crouse = Salmon()

## set harry to an instance of class Halibut
# harry is-a halibut and halibut is-a fish
#harry = Halibut() 
