class human(object):
	pass

class american(human):

	def __init__(self, nation):
		self.nation = nation
		print "In the init of american"

class indian(human):

	def __init__(self, nation):
		self.nation = nation
		print "In the init of indian"

class MH(indian):
	def __init__(self, nation, state):
		super(MH, self).__init__(nation)
		self.state = state
		print "In the init of MH"			

marathi = indian("maharashtra")

newyorker = american("newyork")

punekar = MH("Maharashtra", "Pune")
