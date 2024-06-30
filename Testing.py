class Class():	
	_objlist_ = []
	def __init__ (self, name, year):
		self.name = name
		self.year = year

def Exist(clss, *attr):
	if attr == tuple(clss.__dict__.values()):
		return True
	return False

clss = Class('10 tin 1', '2023')

print(Exist(clss, '10 tin 1', '2023'))