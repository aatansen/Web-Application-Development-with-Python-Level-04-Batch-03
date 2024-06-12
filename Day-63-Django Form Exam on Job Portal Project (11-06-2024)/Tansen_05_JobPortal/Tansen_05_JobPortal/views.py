from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from .forms import *
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            if user.user_type == 'recruiter':
                RecruiterModel.objects.create(
                    user=user
                )
            elif user.user_type == 'seeker':
                SeekerModel.objects.create(
                    user=user
                )
            return redirect('signin')
    else:
        form=CustomUserForm()
    return render(request,'common/signup.html',{'form':form})

def signin(request):
    if request.method=='POST':
        form=CustomUserAuthForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        form=CustomUserAuthForm()
    return render(request,'common/signin.html',{'form':form})

@login_required
def dashboard(request):
    return render(request,'common/dashboard.html')

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def addjob(request):
    current_user=request.user
    if request.method=="POST":
        form=JobForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.created_by=current_user
            form.save()
            return redirect('joblist')
    else:
        form=JobForm()
    return render(request,'recruiter/addjob.html',{'form':form})

@login_required
def joblist(request):
    jobs=JobModel.objects.all()
    jobDict={
        'jobs':jobs
    }
    return render(request,'common/joblist.html',jobDict)

def deletejob(request,jobid):
    job=get_object_or_404(JobModel,id=jobid)
    job.delete()
    return redirect('joblist')

def editjob(request,jobid):
    job=get_object_or_404(JobModel,id=jobid)
    if request.method=="POST":
        form=JobForm(request.POST,instance=job)
        if form.is_valid():
            form.save()
            return redirect('joblist')
    else:
        form=JobForm(instance=job)
    return render(request,'recruiter/editjob.html',{'form':form})

def applyjob(request,jobid):
    # job=JobModel.objects.get(id=jobid)
    current_user=request.user
    job=get_object_or_404(JobModel,id=jobid)
    if request.method=="POST":
        form=JobApplyForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.applied_job=job
            user.applicant=current_user
            user.save()
            return redirect('joblist')
    else:
        form=JobApplyForm()
    return render(request,'seeker/applyjob.html',{'form':form})

def baseprofile(request):
    return render(request,'profile/baseprofile.html')

def basicinfo(request):
    return render(request,'profile/basicinfo.html')

def seekerotherinfo(request):
    return render(request,'profile/seekerotherinfo.html')

def recruiterotherinfo(request):
    return render(request,'profile/recruiterotherinfo.html')

def appliedjob(request):
    current_user=request.user
    # applied_job=get_list_or_404(JobApplyModel,applicant=current_user)
    applied_job=JobApplyModel.objects.filter(applicant=current_user)
    return render(request,'seeker/appliedjob.html',{'applied_job':applied_job})

@login_required
def postedjob(request):
    current_user=request.user
    jobs=JobModel.objects.filter(created_by=current_user)
    return render(request,'recruiter/postedjob.html',{'jobs':jobs})




