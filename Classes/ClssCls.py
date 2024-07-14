from ObjectCls import Object

class Class(Object):	
	_objlist_ = []
	ModList = ("2. Delete class",)

	def __init__ (self, name, year):
		self.name = name
		self.year = year
		self.tchlist = []
		self.stlist = []