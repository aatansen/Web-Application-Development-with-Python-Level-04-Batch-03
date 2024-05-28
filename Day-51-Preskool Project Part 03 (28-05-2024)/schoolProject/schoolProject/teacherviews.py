from django.shortcuts import render,redirect
from schoolApp.models import *

def teacherdashboard(request):
    return render(request,'teacher/teacherdashboard.html')

def teacherlist(request):
    teacher=TeacherAddModel.objects.all()
    teacherDict={
        'teacher':teacher
    }

    return render(request,'teacher/teacherlist.html',teacherDict)

def teacheradd(request):
    department=DepartmentAddModel.objects.all()
    depDict={
        'department':department,
    }
    if request.method=="POST":
        teacher_id=request.POST.get('teacher_id')
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mobile')
        joining_date=request.POST.get('joining_date')
        qualification=request.POST.get('qualification')
        experience=request.POST.get('experience')
        department_id=request.POST.get('department_id')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        repeat_password=request.POST.get('repeat_password')
        profile_image=request.FILES.get('profile_image')
        present_address=request.POST.get('present_address')
        permanent_address=request.POST.get('permanent_address')
        
        dept=DepartmentAddModel.objects.get(id=department_id)
        
        if password==repeat_password:
            user = CustomUserModel.objects.create_user(
                email=email,
                username=username,
                password=password,
                user_type='2'
            )
            user.save()
        
            teacher=TeacherAddModel(
                user=user,
                teacher_id=teacher_id,
                name=name,
                gender=gender,
                mobile=mobile,
                joining_date=joining_date,
                qualification=qualification,
                experience=experience,
                myDepartment=dept,
                profile_image=profile_image,
                present_address=present_address,
                permanent_address=permanent_address,
            )
            teacher.save()
            return redirect('teacherlist')
    return render(request,'teacher/teacheradd.html',depDict)

def teacherdetails(request):
    return render(request,'teacher/teacherdetails.html')

def teacheredit(request):
    return render(request,'teacher/teacheredit.html')

def teacherdelete(request,teaUser):
    teacher=CustomUserModel.objects.get(username=teaUser)
    teacher.delete()
    return redirect('teacherlist')