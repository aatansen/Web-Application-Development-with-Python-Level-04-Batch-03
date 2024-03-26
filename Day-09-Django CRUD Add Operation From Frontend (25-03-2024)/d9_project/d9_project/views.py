from django.shortcuts import render,redirect
from studentapp.models import studentModel,markModel,teacherModel,subjectModel,universityModel

def student(request):
    student=studentModel.objects.all()
    myDict={
        'student':student
    }
    return render(request,'student.html',myDict)

def addstudent(request):
    if request.method=='POST':
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        
        student=studentModel(
            Name=name,
            Department=department,
            City=city,
        )
        
        student.save()
        return redirect('student')
    return render(request,'addstudent.html')

def mark(request):
    mark=markModel.objects.all()
    myDict={
        'mark':mark
    }
    return render(request,'mark.html',myDict)

def addmark(request):
    if request.method=='POST':
        name=request.POST.get('name')
        roll=request.POST.get('roll')
        mark=request.POST.get('mark')
        
        mark=markModel(
           Name=name,
           Roll=roll,
           Mark=mark,
        )
        mark.save()
        return redirect('mark')
    return render(request,'addmark.html')

def teacher(request):
    teacher=teacherModel.objects.all()
    myDict={
        'teacher':teacher
    }
    return render(request,'teacher.html',myDict)

def addteacher(request):
    if request.method=='POST':
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        
        teacher=teacherModel(
            Name=name,
            Department=department,
            City=city,
        )
        teacher.save()
        return redirect('teacher')
    return render(request,'addteacher.html')

def subject(request):
    subject=subjectModel.objects.all()
    myDict={
        'subject':subject
    }
    return render(request,'subject.html',myDict)

def addsubject(request):
    if request.method=='POST':
        name=request.POST.get('name')
        category=request.POST.get('category')
        mark=request.POST.get('mark')
        
        subject=subjectModel(
            Name=name,
            Category=category,
            Mark=mark,
        )
        subject.save()
        return redirect('subject')
    return render(request,'addsubject.html')

def university(request):
    university=universityModel.objects.all()
    myDict={
        'university':university
    }
    return render(request,'university.html',myDict)

def adduniversity(request):
    if request.method=='POST':
        rank=request.POST.get('rank')
        name=request.POST.get('name')
        location=request.POST.get('location')
        
        university=universityModel(
            Rank=rank,
            Name=name,
            Location=location,
        )
        
        university.save()
        return redirect('university')
    return render(request,'adduniversity.html')