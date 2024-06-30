import Output
import Func
import time
from ObjectCls import Object
from ClssCls import Class
from TeacherCls import Teacher
from StudentCls import Student

namelist = ('class', 'teacher', 'student')

while True:
	time.sleep(1)
	Output.menu()
	action_index = int(input())
	if action_index > 9 or action_index < 0 or not isinstance(action_index, int):
		print("The input seems wrong! Try again")
		continue

	class_index = (action_index - 1)%3
	if action_index == 0: #Stop
		break

	elif action_index == 1: #New class
		name = input("Class name: ")
		year = input("Class of: ")
		Func.CreateObj(class_index, name, year)

	elif action_index == 2: #New teacher
		name = input("Teacher's name: ")
		year = input("Teacher's birthday ( MM/DD/YY): ")
		subject = input("Teacher's subject: ")
		Func.CreateObj(class_index, name, year, subject)

	elif action_index == 3: #New student
		if len(Object.classlist[0]._objlist_) == 0:
			print("Can't assign new student due to no class assigned")
			continue
		name = input("Students name: ")
		year = input("Students birthday ( MM/DD/YY): ")
		Output.choose_obj_menu(0) #Choose student's class
		clss = Object.classlist[0]._objlist_[int(input()) - 1]
		Func.CreateObj(class_index, name, year, clss)

	elif action_index < 7: #Modify object
		if len(Object.classlist[class_index]._objlist_) == 0:
			print(f"Cannot make modification due to no {namelist[class_index]} assigned")
			continue
		Output.choose_obj_menu(class_index)
		obj_index = int(input()) - 1
		Output.choose_mod_type(class_index)
		mod_index = int(input())
		if mod_index == 1: #Change basic infos
			name = input("Input name: ")
			year = input("Input year or birthday: ")
			Func.AlterInfo(class_index, obj_index, name, year)

		elif mod_index == 2:
			del Object.classlist[class_index]._objlist_[obj_index]

		elif mod_index == 4:
			Output.choose_tch_clss(obj_index) #Choose teacher's class
			clss = Object.classlist[0]._objlist_[int(input()) - 1]
			Object.classlist[1]._objlist_[obj_index].rmvfromclss(clss)

		elif mod_index == 3:
			Output.choose_obj_menu(0) #Choose class
			clss = Object.classlist[0]._objlist_[int(input()) - 1]
			if class_index == 1: #Is teacher
				Func.AddTchToClss(obj_index, clss)
			elif class_index == 2: #Is student
				Func.ChangeStClss(obj_index, clss)

	else:
		Output.choose_obj_menu(class_index)
		obj = Object.classlist[class_index]._objlist_[int(input()) - 1]
		obj.getinfo()



