from django.shortcuts import render,redirect,HttpResponse
from studentapp.models import studentModel

def student(request):
    student=studentModel.objects.all()
    myDict={
        'student':student
    }
    return render(request,'student.html',myDict)

def addstudent(request):
    if request.method=="POST":
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        studentImage=request.FILES.get('studentImage')

        student=studentModel(
            Name=name,
            Department=department,
            City=city,
            Image=studentImage,
        )
        student.save()
        return redirect('student')

    return render(request,'addstudent.html')

def viewstudent(request,myid):
    student=studentModel.objects.get(id=myid)
    print(f"This is object id: {myid}")
    myDict={
        'student':student,
    }
    return render(request,'viewstudent.html',myDict)

def portfolio(request):
    return render(request,'index.html')

