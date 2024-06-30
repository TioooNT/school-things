from ObjectCls import Object

namelist = ('Class', 'Teacher', 'Student')

def Exist(objclass, *attr):
	for obj in objclass._objlist_:
		if attr == tuple(obj.__dict__.values())[:len(attr)]:
			return True
	return False


def TchInClss(teacher, clss):
	if clss in teacher.clsslist:
		return True
	return False


def CreateObj(class_index, *attr):
	objclass = Object.classlist[class_index]
	if Exist(objclass, *attr):
		print(f"{namelist[class_index]}'s already existed")
		return
	objclass._objlist_.append(objclass(*attr))


def AlterInfo(class_index, obj_index, *attr):
	objclass = Object.classlist[class_index]
	if Exist(objclass, *attr):
		print(f"{namelist[class_index]}'s already existed")
		return
	Object.classlist[class_index]._objlist_[obj_index].alterinfo(*attr)


def AddTchToClss(tch_index, clss):
	teacher = Object.classlist[1]._objlist_[tch_index]
	if TchInClss(teacher, clss):
		print("Teacher's already in this class")
		return
	teacher.addclss(clss)


def ChangeStClss(st_index, clss):
	student = Object.classlist[2]._objlist_[st_index]
	if student.clss == clss:
		print("Student's already in this class")
		return
	student.clsschange(clss)
