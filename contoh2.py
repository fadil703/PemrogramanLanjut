class Person:
	total = 0
	def __init__(self, name):
		self.name = name
		Person.total += 1

	def __del__(self):
		Person.total -= 1

	def sayHalo(self):
		print('Halo, my name is %s, apa how are you?' %self.name)

	def total_population(cls):
		print('Total population %s' % cls.total)

	total_population = classmethod(total_population)

prs = Person('budi')
prs.sayHalo()
Person.total_population()

prs2 = Person('andi')
prs2.sayHalo()
Person.total_population()

print ('budi deleted')
del prs

Person.total_population()