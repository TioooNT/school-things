import time
from Manipulators import Operator, Output
from Classes.ObjectCls import Object
from Classes.ClssCls import Class
from Classes.TeacherCls import Teacher
from Classes.StudentCls import Student

namelist = ('class', 'teacher', 'student')

school = Operator()

while True:
	time.sleep(1)

	Output.menu()
	action_index = int(input()) #Input action
	
	#Check wrong input
	if action_index > 9 or action_index < 0 or not isinstance(action_index, int):
		print("The input seems wrong! Try again")
		continue

	obj_class = Object.classlist[(action_index - 1)%3]
	if action_index == 0: #Stop
		break

	elif action_index == 1: #New class
		name = input("Class name: ")
		year = input("Class of: ")

		school.CreateObj(obj_class, name, year)

	elif action_index == 2: #New teacher
		name = input("Teacher's name: ")
		year = input("Teacher's birthday ( MM/DD/YY): ")
		subject = input("Teacher's subject: ")

		school.CreateObj(obj_class, name, year, subject)

	elif action_index == 3: #New student
		if len(Class._objlist_) == 0:
			print("Can't assign new student due to no class assigned")
			continue

		name = input("Students name: ")
		year = input("Students birthday ( MM/DD/YY): ")

		Output.choose_obj_menu(0) #Choose student's class
		clss = Class._objlist_[int(input()) - 1]

		school.CreateObj(obj_class, name, year, clss)

	elif action_index < 7: #Modify object

		if len(obj_class._objlist_) == 0:
			print(f"Cannot make modification due to no {obj_class().class_name()} assigned")
			continue

		Output.choose_obj_menu(obj_class, None) #Choose object to modify
		obj_index = int(input()) - 1

		Output.choose_mod_type(obj_class) #Choose modification's type
		mod_index = int(input())

		if mod_index == 1: #Change basic infos
			name = input("Input name: ")
			year = input("Input year or birthday: ")

			school.AlterInfo(obj_class, obj_index, name, year)

		elif mod_index == 2:
			del obj_class._objlist_[obj_index]

		elif mod_index == 4:

			Output.choose_obj_clss(Class, ) #Choose teacher's class
			clss = Class._objlist_[int(input()) - 1]

			Teacher._objlist_[obj_index].rmvfromclss(clss)

		elif mod_index == 3:

			Output.choose_obj_menu(Class, Teacher._objlist_[obj_index].subject) #Choose class
			clss = Class._objlist_[int(input()) - 1]

			if isinstance(obj_class(), Teacher): #Is teacher
				school.AddTchToClss(obj_index, clss)

			elif isinstance(obj_class(), Student): #Is student
				school.ChangeStClss(obj_index, clss)

	else:

		Output.choose_obj_menu(obj_class, None)
		obj = obj_class._objlist_[int(input()) - 1]

		obj.getinfo()



