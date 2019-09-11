class Puppy:
	def __init__(self):
		self.name = []
		self.color = []

	def __setitem__(self, name, color):
		self.name.append(name)
		self.color.append(color)

	def __getitem__(self, name):
		if name in self.name:
			return self.color[self.name.index(name)]
			
		else:
			return none


dog = Puppy()

dog['max'] = 'brown'
dog['ruby'] = 'black'

print ('ruby is', dog['ruby'])
