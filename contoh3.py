class SchoolMember:
	def __init__(self, name, age):
		self.name = name
		self.age = age

		print ('create new school member: %s' % self.name)

	def info(self):
		print ('Name: %s, Age: %s' % (self.name, self.age))

class Teacher(SchoolMember):
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary

		print ('create teacher: %s' % self.name)

	def info(self):
		SchoolMember.info(self)
		print ('salary: %s' % self.salary)

class Student(SchoolMember):
	def __init__(self, name, age, grade):
		SchoolMember.__init__(self, name, age)
		self.grade = grade
		print ('create student: %s' % self.name)

	def info(self):
		SchoolMember.info(self)
		print ('grade: %s' % self.grade)
tchr = Teacher('budi', 40, 300000)
stdnt = Student('Andi', 20, 90)
print()
member = [tchr, stdnt]
for person in member:
	person.info()