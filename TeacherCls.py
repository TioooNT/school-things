from PersonCls import Person


class Teacher(Person):
	_objlist_ = []
	def __init__ (self, name, year, subject):
		super().__init__(name, year)
		self.subject = subject
		self.clsslist = []

	def addclss (self, clss):
		self.clsslist.append(clss)
		clss.tchlist.append(self)


	def rmvfromclss (self, clss):
		self.clsslist.remove(clss)
		clss.tchlist.remove(self)
		