class Person:
	def __init__(self, name):
		self.name = name

	def sayHalo(self):
		print('halo, my name is %s how are you?' % self.name)


prs = Person('budi')
prs.sayHalo()


