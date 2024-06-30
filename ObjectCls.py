class Object():
	def getinfo (self):
		
		#Is a class
		if isinstance(self, Class):
			print(f"Class name: {self.name}")
			print(f"Class of: {self.year}")
			print(f"Class size: {len(self.stlist)}")
			if len(self.tchlist) == 0:
				print("Teacher list: None")
			else:
				print("Teacher list:")
				for teacher in self.tchlist:
					print(f"- {teacher.name}: {teacher.subject}")
			return

		#Is a person
		print(f"- Name: {self.name}")
		print(f"- Birthday: {self.year}")

		#Is a teacher
		if isinstance(self, Teacher):
			print(f"Teacher's subject: {self.subject}")
			print("Teacher's class list: ", end = "")
			print("None" if len(self.clsslist) == 0 else [f"{clss.name} {clss.year}" for clss in self.clsslist])
			return

		#Is a Student
		print(f"Student's class: {self.clss.name}")
		print(f"Class of: {self.clss.year}")
		print(f"Teacher list:")
		if len(self.clss.tchlist) == 0:
				print("Teacher list: None")
		else:
			print("Teacher list:")
			for teacher in self.clss.tchlist:
				print(f"- {teacher.name}: {teacher.subject}")

	def alterinfo (self, name, year):
		self.name = name
		self.year = year

from ClssCls import Class
from TeacherCls import Teacher
from StudentCls import Student

Object.classlist = [Class, Teacher, Student]