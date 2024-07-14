from PersonCls import Person


class Teacher(Person):
	_objlist_ = []
	ModList = ('2. Delete teacher', '3. Add teacher to a class', '4. Remove teacher from a class')

	def __init__ (self, name, year, subject):
		super().__init__(name, year)
		self.subject = subject
		self.clsslist = []

	def addclss (self, clss) -> None:
		self.clsslist.append(clss)
		clss.tchlist.append(self)


	def rmvfromclss (self, clss) -> None:
		self.clsslist.remove(clss)
		clss.tchlist.remove(self)
		