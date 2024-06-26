from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from jobApp.models import *
from django.db.models import Q


message_box={
    'signup_success':'Signup successful!',
    'password_warning':'Password and confirm not matched!',
}

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        user_type=request.POST.get('user_type')
        city=request.POST.get('city')
        gender=request.POST.get('gender')
        profile_picture=request.FILES.get('profile_picture')
        email=request.POST.get('email')

        if password==confirm_password:
            user = CustomUserModel.objects.create_user(
                username=username,
                password=password,
                user_type=user_type,
                city=city,
                gender=gender,
                profile_picture=profile_picture,
                email=email,
            )
            user.save()
            if user_type=="recruiter":
                user_tp=RecruiterModel.objects.create(recruiter_user=user)
            if user_type=="seeker":
                user_tp=SeekerModel.objects.create(seeker_user=user)
            user_tp.save()
            messages.success(request,message_box['signup_success'])
            return redirect('signin')
        else:
            messages.success(request,message_box['password_warning'])
            return redirect('signup')
    return render(request,'common/signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(
            username=username,
            password=password,
        )
        print(f"The auth user is: {user}")
        if user:
            login(request,user)
            return redirect('dashboard')
    return render(request,'common/signin.html')

@login_required
def dashboard(request):
    return render(request,'common/dashboard.html')

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def addjob(request):
    if request.method=='POST':
        job_title=request.POST.get('job_title')
        company_description=request.POST.get('company_description')
        company_logo=request.FILES.get('company_logo')
        company_name=request.POST.get('company_name')
        company_location=request.POST.get('company_location')
        qualifications=request.POST.get('qualifications')
        deadline=request.POST.get('deadline')
        salary=request.POST.get('salary')
        
        job=JobModel.objects.create(
            job_title=job_title,
            company_description=company_description,
            company_logo=company_logo,
            company_name=company_name,
            company_location=company_location,
            qualifications=qualifications,
            deadline=deadline,
            salary=salary,
            created_by=request.user
        )
        job.save()
        return redirect('viewjob')
    return render(request,'recruiter/addjob.html')

def viewjob(request):
    # change apply button for seeker when already applied 
    jobs = JobModel.objects.all()
    job_filtered=[]
    for i in jobs:
        already_applied=ApplyJobModel.objects.filter(applicant=request.user,applied_job=i)
        job_filtered.append(
            (i,already_applied),
        )
    jobDict={
        'job_filtered':job_filtered
    }
    return render(request,'common/viewjob.html',jobDict)

@login_required
def editjob(request,jobid):
    jobs=JobModel.objects.get(id=jobid)
    print(f"This is the selected job: {jobs.company_logo}")
    jobDict={
        'jobs':jobs
    }
    if request.method=="POST":
        job_title=request.POST.get('job_title')
        company_description=request.POST.get('company_description')
        company_logo=request.FILES.get('company_logo')
        company_name=request.POST.get('company_name')
        company_location=request.POST.get('company_location')
        qualifications=request.POST.get('qualifications')
        deadline=request.POST.get('deadline')
        salary=request.POST.get('salary')

        print(f"This is my image: {company_logo}")
        if company_logo:
            job=JobModel(
                id=jobid,
                job_title=job_title,
                company_description=company_description,
                company_logo=company_logo,
                company_name=company_name,
                company_location=company_location,
                qualifications=qualifications,
                deadline=deadline,
                salary=salary,
                created_by=request.user
            )
        else:
            job=JobModel(
                id=jobid,
                job_title=job_title,
                company_description=company_description,
                company_logo=jobs.company_logo,
                company_name=company_name,
                company_location=company_location,
                qualifications=qualifications,
                deadline=deadline,
                salary=salary,
                created_by=request.user
            )
        job.save()
        return redirect('viewjob')
    return render(request,'recruiter/editjob.html',jobDict)

@login_required
def deletejob(request,jobid):
    job=JobModel.objects.get(id=jobid)
    job.delete()
    return redirect('viewjob')

@login_required
def baseprofile(request):
    return render(request,'profile/baseprofile.html')

@login_required
def profileinfo(request):
    return render(request,'profile/profileinfo.html')

@login_required
def basicprofile(request):
    
    return render(request,'profile/basicprofile.html')

@login_required
def recruitercontact(request):
    return render(request,'profile/recruitercontact.html')


@login_required
def seekereducation(request):
    return render(request,'profile/seekereducation.html')

@login_required
def seekerwork(request):
    return render(request,'profile/seekerwork.html')

@login_required
def changepassword(request):
    current_user=request.user
    if request.method=="POST":
        current_pass=request.POST.get('current_pass')
        new_pass=request.POST.get('new_pass')
        confirm_new_pass=request.POST.get('confirm_new_pass')
        
        pass_check = check_password(current_pass,current_user.password)
        if pass_check:
            if new_pass==confirm_new_pass:
                current_user.set_password(new_pass)
                current_user.save()
                update_session_auth_hash(request,current_user)
                return redirect('baseprofile')
    return render(request,'profile/changepassword.html')

@login_required
def specificjobpost(request):
    current_user=request.user
    
    if current_user.user_type == "recruiter":
        jobs = JobModel.objects.filter(created_by=current_user)
        
        jobDict={
            'jobs':jobs
        }
    return render(request,'profile/specificjobpost.html',jobDict)

@login_required
def editprofile(request):
    if request.method == "POST":
        username=request.POST.get('username')
        user_type=request.POST.get('user_type')
        city=request.POST.get('city')
        gender=request.POST.get('gender')
        profile_picture=request.FILES.get('profile_picture')
        profile_picture=request.POST.get('profile_picture')
    return render(request,'profile/editprofile.html')

@login_required
def applyjob(request,jobid):
    job=get_object_or_404(JobModel,id=jobid)
    jobDict={
        'job':job
    }
    
    already_applied=ApplyJobModel.objects.filter(applicant=request.user,applied_job=job).exists()
    if already_applied:
        messages.warning(request,"Already applied")
        return redirect('viewjob')
    
    if request.method=="POST":
        skills=request.POST.get('skills')
        resume=request.FILES.get('resume')
        seeker_profile_pic=request.FILES.get('seeker_profile_pic')
        qualifications=request.POST.get('qualifications')
        
        job_apply=ApplyJobModel.objects.create(
            skills=skills,
            resume=resume,
            seeker_profile_pic=seeker_profile_pic,
            qualifications=qualifications,
            applicant=request.user,
            applied_job=job,
        )
        job_apply.save()
        return redirect('viewjob')
    jobDict['already_applied'] = already_applied
    return render(request,'seeker/applyjob.html',jobDict)

def appliedjob(request):
    # jobs=JobModel.objects.all()
    # all_applied_job=[]
    # for job in jobs:
    #     appliedjob=ApplyJobModel.objects.filter(applied_job=job)
        
    #     if appliedjob:
    #         all_applied_job.append(job)
        
    
    # jobDict={
    #     'all_applied_job':all_applied_job
    # }
    
    current_user=request.user
    appliedjob = ApplyJobModel.objects.filter(applicant=current_user)
    jobDict={
        'appliedjob':appliedjob
    }
    
    
    return render(request,'seeker/appliedjob.html',jobDict)


def applicants(request,jobid):
    job=JobModel.objects.get(id=jobid)

    applicants=ApplyJobModel.objects.filter(applied_job=job)
        
    jobDict={
        'applicants':applicants,
        'job':job,
    }
    return render(request,'recruiter/applicants.html',jobDict)

def jobreject(request,jobid):
    job =ApplyJobModel.objects.get(id=jobid)
    job.status="Rejected"
    job.save()
    jobid_red=job.id
    return redirect(f'applicants',jobid_red)

# def jobcallinterview(request,jobid):
#     job =ApplyJobModel.objects.get(id=jobid)
#     job.status="Approved"
#     job.save()
#     return redirect('applicants',jobid=job.applicant.id)

# to select a date for interview
def jobcallinterview(request,jobid):
    job =ApplyJobModel.objects.get(id=jobid)
    job.status="Approved"
    job.save()
    return redirect('datefix')

def datefix(request):
    return render(request,'recruiter/datefix.html')

def callforinterview(request):
    return render(request,'recruiter/callforinterview.html')

def searchpage(request):
    
    # search option 
    search=request.GET.get('search')
    # jobs = JobModel.objects.filter(job_title=search)
    jobs = JobModel.objects.filter(
        Q(job_title__icontains=search)|
        Q(deadline__icontains=search)|
        Q(created_by__username__icontains=search)
        )
    # change apply button for seeker when already applied 
    job_filtered=[]
    for i in jobs:
        already_applied=ApplyJobModel.objects.filter(applicant=request.user,applied_job=i)
        job_filtered.append(
            (i,already_applied),
        )
    jobDict={
        'job_filtered':job_filtered
    }
    return render(request,'common/searchpage.html',jobDict)
