from ObjectCls import Object

class Class(Object):	
	_objlist_ = []
	def __init__ (self, name, year):
		self.name = name
		self.year = year
		self.tchlist = []
		self.stlist = []