from ObjectCls import Object

namelist = ('class', 'teacher', 'student')
modtypelist = (
		("2. Delete class",),
		('2. Delete teacher', '3. Add teacher to a class', '4. Remove teacher from a class'),
		('2. Delete student', "3. Change student's class"),
	)


def menu():
	print("Choose action:")
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


def choose_obj_menu (class_index):
	print(f"Choose {namelist[class_index]}:")
	Class = Object.classlist[class_index]
	for cnt in range(len( Class._objlist_ ) ):
		print(f"{cnt+1}. {Class._objlist_[cnt].name} {Class._objlist_[cnt].year}")


def choose_mod_type (class_index):
	print(f"1. Change {namelist[class_index]}'s basic informations")
	for modtype in modtypelist[class_index]:
		print(str(modtype))


def choose_tch_clss (obj_index):
	print("Choose class:")
	Teacher = Object.classlist[1]._objlist_[obj_index]
	for cnt in range(len(Teacher.clsslist)):
		print(f"{cnt+1}. {Teacher.clsslist[cnt].name} {Teacher.clsslist[cnt].year}")
