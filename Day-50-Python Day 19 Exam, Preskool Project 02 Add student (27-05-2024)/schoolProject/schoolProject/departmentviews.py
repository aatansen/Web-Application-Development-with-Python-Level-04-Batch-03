from django.shortcuts import render,redirect

def departmentslist(request):
    return render(request,'department/departmentslist.html')

def departmentsadd(request):
    return render(request,'department/departmentsadd.html')

def departmentsedit(request):
    return render(request,'department/departmentsedit.html')

def departmentsdelete(request):
    return redirect('departmentslist')