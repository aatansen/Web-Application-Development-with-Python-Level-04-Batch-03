from django.shortcuts import render,redirect
from schoolApp.models import *

def subjectslist(request):
    subject=SubjectModel.objects.all()
    subDict={
        'subject':subject
    }
    return render(request,'subject/subjectslist.html',subDict)

def subjectsadd(request):
    department=DepartmentAddModel.objects.all()
    deptDict={
        'department':department
    }
    
    if request.method=="POST":
        sub_id=request.POST.get('sub_id')
        sub_name=request.POST.get('sub_name')
        Department_ID=request.POST.get('Department_ID')
        
        dept=DepartmentAddModel.objects.get(id=Department_ID)
        
        subject=SubjectModel.objects.create(
            sub_id=sub_id,
            sub_name=sub_name,
            myDepartment=dept,
        )
        subject.save()
        return redirect('subjectslist')
    
    
    return render(request,'subject/subjectsadd.html',deptDict)

def subjectsedit(request):
    return render(request,'subject/subjectsedit.html')

def subjectsdelete(request):
    return redirect('subjectslist')