# class inheritance sample code

# the base or super class
class SchoolMember(object):
	'''represents any school member'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def detail(self):
		'''show name and age, stay on same line (trailing comma)'''
		print 'Name: %-13s Age: %s' % (self.name, self.age),
		
# use the base class as argument to ingerit from
class Teacher(SchoolMember):
	'''represents a teacher'''
	def __init__(self, name, age, subject):
		# call the base class constructor
		# it assigns name, age to self.name, self.age
		SchoolMember.__init__(self, name, age)
		self.subject = subject
		
	def detail(self):
		'''teaches this course'''
		SchoolMember.detail(self)
		print 'Teaches course: %s ' % self.subject

class Student(SchoolMember):
	'''represents a student'''
	def __init__(self, name, age, grades):
		SchoolMember.__init__(self, name, age)
		self.grades = grades
		
	def detail(self):
		'''student grades'''
		SchoolMember.detail(self)
		print 'Average grades: %d' % self.grades
		
# teacher has name age and subject taught
t1 = Teacher('Mr. Schard', 40, 'Beginning Python 101')
# student has name, age and average grade (max 100)
s1 = Student('Abigale Agat', 20, 92)
s2 = Student('Bertha Belch', 22, 65)
s3 = Student('Karl Kuss', 21, 98)
s4 = Student('Tom Tippit', 22, 77)
s5 = Student('Zoe Zeller', 20, 88)

print '-' * 55

#list of instances, Teacher t1 and Students s1 ... s5
members = [t1, s2, s3, s4, s5]
sumgrades = 0
for member in members:
	memberType = member.detail()
	try:
		sumgrades += member.grades
	except AttributeError:
		pass # this would be a teacher, has no grades so skip

print "\n%s's students class-average grades = %d" % (t1.name, sumgrades/5)

"""
output -->
Name: Mr. Schard	Age: 40 Teaches course: Beginning Python 101
Name: Abigale Agat	Age: 20 Average grades: 92
Name: Bertha Belch 	Age: 22 Average grades: 65
Name: Karl Kuss		Age: 21 Average grades: 98
Name: Tom Tippit	Age: 22	Average grades: 77
Name: Zoe Zeller	Age: 20	Average grades: 88

Mr. Schard's students class-average grades = 84
"""