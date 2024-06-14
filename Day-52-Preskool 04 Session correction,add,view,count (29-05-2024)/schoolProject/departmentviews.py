from django.shortcuts import render,redirect
from schoolApp.models import *

def departmentslist(request):
    department=DepartmentAddModel.objects.all()
    departmentList=[]
    for i in department:
        student_count = StudentAddModel.objects.filter(myDepartment=i).count()
        teacher_count = TeacherAddModel.objects.filter(myDepartment=i).count()
        print(student_count)
        
        departmentList.append(
            {
                'Department_Name':i.Department_Name,
                'Head_of_Department':i.Head_of_Department,
                'student_count':student_count,
                'teacher_count':teacher_count,
                'id':i.id,
            }
        )
        
    departmentDict={
        'departmentList':departmentList,
    }
    return render(request,'department/departmentslist.html',departmentDict)

def departmentsadd(request):
    if request.method=="POST":
        Department_Name=request.POST.get('Department_Name')
        Head_of_Department=request.POST.get('Head_of_Department')
        
        dept=DepartmentAddModel.objects.create(
            Department_Name=Department_Name,
            Head_of_Department=Head_of_Department,
        )
        dept.save()
        return redirect('departmentslist')
    return render(request,'department/departmentsadd.html')

def departmentsedit(request):
    return render(request,'department/departmentsedit.html')

def departmentsdelete(request,deptid):
    dept=DepartmentAddModel.objects.get(id=deptid)
    dept.delete()
    return redirect('departmentslist')