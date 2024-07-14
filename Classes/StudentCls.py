from PersonCls import Person

class Student(Person):
	_objlist_ = []
	ModList = ('2. Delete student', "3. Change student's class")

	def __init__ (self, name, year, clss):
		super().__init__(name, year)
		self.clss = clss
		self.clss.stlist.append(self)



	def clsschange (self, toclss) -> None:
		self.clss.stlist.remove(self)
		self.clss = toclss
		self.clss.stlist.append(self)