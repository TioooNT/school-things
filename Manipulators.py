from Classes.ClssCls import Class
from Classes.TeacherCls import Teacher
from Classes.StudentCls import Student


class Checker:

	@staticmethod
	def Exist(obj_class, *attr) -> bool:

		for obj in obj_class._objlist_:
			if attr == tuple(obj.__dict__.values())[:len(attr)]:
				return True
			
		return False

	@staticmethod
	def TchInClss(teacher: Teacher, clss: Class) -> bool:
		if clss in teacher.clsslist:
			return True
		
		return False

	@staticmethod
	def SubInClss(subject: str, tchlist: list[Teacher]) -> bool:
		for teacher in tchlist:
			if subject == teacher.subject:
				return True
			
		return False



class Output:

	@staticmethod
	def menu () -> None:
		print("====== Menu ======")
		print("0. Stop the program")
		print("1. New class")
		print("2. New teacher")
		print("3. New student")
		print("4. Modify class's informations")
		print("5. Modify teacher's informations")
		print("6. Modify student's informations")
		print("7. Get class's informations")
		print("8. Get teacher's informations")
		print("9. Get student's informations")
		print("Choose action:", end = " ")

	@staticmethod
	def choose_obj_menu (obj_class, tch_subject: str) -> None:
		print(f"Choose { obj_class().class_name() }:")

		"""

			tch_subject is always None except when we are choosing class for teacher to teach
			If tch_subject's already been taught in the chosen class, ignore it

		"""

		for index in range(len( obj_class._objlist_ ) ):
			if tch_subject != None and Checker.SubInClss(tch_subject, Class._objlist_[index].tchlist) == True:
				continue
			print(f"{index+1}. {obj_class._objlist_[index].name} {obj_class._objlist_[index].year}")


	@staticmethod
	def choose_mod_type (obj_class) -> None:
		print(f"1. Change {obj_class().class_name()}'s basic informations")

		for modtype in obj_class().ModList:
			print(str(modtype))





class Operator:

	def CreateObj(self, obj_class, *attr) -> None:

		if Checker.Exist(obj_class, *attr):
			print(f"{obj_class().class_name()}'s already existed")
			return
		
		obj_class._objlist_.append(obj_class(*attr))


	def AlterInfo(self, obj_class, obj_index: int, *attr) -> None:

		if Checker.Exist(obj_class, *attr):
			print(f"{obj_class().class_name()}'s already existed")
			return
		
		obj_class._objlist_[obj_index].alterinfo(*attr)


	def AddTchToClss(self, tch_index: int, clss: Class) -> None:
		teacher = Teacher._objlist_[tch_index]

		if self.TchInClss(teacher, clss):
			print("Teacher's already in this class")
			return
		
		teacher.addclss(clss)


	def ChangeStClss(self, st_index: int, clss: Class) -> None:
		student = Student._objlist_[st_index]

		if student.clss == clss:
			print("Student's already in this class")
			return
		
		student.clsschange(clss)

