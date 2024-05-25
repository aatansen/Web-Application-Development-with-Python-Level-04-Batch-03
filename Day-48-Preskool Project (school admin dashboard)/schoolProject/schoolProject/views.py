from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from schoolApp.models import CustomUserModel

def signuppage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            user = CustomUserModel.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()
            return redirect('signinpage')
    return render(request,'common/signuppage.html')

def signinpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(
            username=username,
            password=password
            )
        if authenticate:
            login(request,user)
            return redirect('homepage')
    return render(request,'common/signinpage.html')

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signinpage')

@login_required
def homepage(request):
    return render(request,'common/homepage.html')

def adminpage(request):
    return render(request,'myadmin/adminpage.html')

def teacherdashboard(request):
    return render(request,'teacher/teacherdashboard.html')

def studentdashboard(request):
    return render(request,'student/studentdashboard.html')

def studentlist(request):
    return render(request,'student/studentlist.html')

def studentadd(request):
    return render(request,'student/studentadd.html')

def studentdetails(request):
    return render(request,'student/studentdetails.html')

def studentedit(request):
    return render(request,'student/studentedit.html')

def studentadelete(request):
    return redirect('studentlist')

def teacherlist(request):
    return render(request,'teacher/teacherlist.html')

def teacheradd(request):
    return render(request,'teacher/teacheradd.html')

def teacherdetails(request):
    return render(request,'teacher/teacherdetails.html')

def teacheredit(request):
    return render(request,'teacher/teacheredit.html')

def teacherdelete(request):
    return redirect('teacherlist')

def departmentslist(request):
    return render(request,'department/departmentslist.html')

def departmentsadd(request):
    return render(request,'department/departmentsadd.html')

def departmentsedit(request):
    return render(request,'department/departmentsedit.html')

def departmentsdelete(request):
    return redirect('departmentslist')

def subjectslist(request):
    return render(request,'subject/subjectslist.html')

def subjectsadd(request):
    return render(request,'subject/subjectsadd.html')

def subjectsedit(request):
    return render(request,'subject/subjectsedit.html')

def subjectsdelete(request):
    return redirect('subjectslist')




























