class student(object):

	def __init__(self, roll_no, age):
		self.roll_no = roll_no
		self.age = age
	
	def print_roll_no(self):
		print "Roll_no is %r" %(self.roll_no)
		print "Age is %r" %(self.age)


Ram = student(24, 11)
Laxman = student(45, 9)

Ram.print_roll_no()
Laxman.print_roll_no()
