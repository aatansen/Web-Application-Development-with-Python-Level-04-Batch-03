from django.shortcuts import render,redirect

def signuppage(request):
    return render(request,'common/signuppage.html')

def signinpage(request):
    return render(request,'common/signinpage.html')

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




























