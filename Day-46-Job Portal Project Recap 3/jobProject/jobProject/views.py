from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from jobApp.models import CustomUserModel,RecruiterProfileModel,SeekerProfileModel,SeekerEducationModel,SeekerWorkExModel,BasicInfoModel,ContactModel,AddJobModel

def signup(request):
    if request.method == "POST":
        profilePhoto = request.FILES.get('profilePhoto')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        country = request.POST.get('country')
        bloodGroup = request.POST.get('bloodGroup')
        userType = request.POST.get('userType')
        
        if password==confirmPassword:
            user = CustomUserModel.objects.create_user(
                profilePhoto=profilePhoto,
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                age=age,
                gender=gender,
                city=city,
                country=country,
                bloodGroup=bloodGroup,
                userType=userType,
            )
            if user.userType=='recruiter':
                RecruiterProfileModel.objects.create(user=user)
            elif user.userType=='seeker':
                SeekerProfileModel.objects.create(user=user)
                SeekerEducationModel.objects.create(user=user)
                SeekerWorkExModel.objects.create(user=user)

            BasicInfoModel.objects.create(user=user)
            ContactModel.objects.create(user=user)
            user.save()
            return redirect('signin')
    return render(request,"signup.html")

def signin(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(
            username=username,
            password=password
        )
        if user:
            login(request,user)
            return redirect('dashboard')
    return render(request,'signin.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')

def logoutpage(request):
    logout(request)
    return redirect('signin')

def profile(request):
    return render(request,'profile.html')

def profileinfo(request):
    return render(request,'profileinfo.html')

def recruiterprofile(request):
    return render(request,'recruiter/recruiterprofile.html')

def seekerprofile(request):
    return render(request,'seeker/seekerprofile.html')

def seekereducation(request):
    return render(request,'seeker/seekereducation.html')

def seekerworkex(request):
    return render(request,'seeker/seekerworkex.html')

def basicinfo(request):
    return render(request,'basicinfo.html')

def contactinfo(request):
    return render(request,'contactinfo.html')

def editprofile(request):
    if request.method == "POST":
        profile_photo = request.FILES.get("profile_photo")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        country = request.POST.get("country")
        bloodGroup = request.POST.get("bloodGroup")
        userType = request.POST.get("userType")
        father_name = request.POST.get("father_name")
        mother_name = request.POST.get("mother_name")
        hobby = request.POST.get("hobby")
        languages = request.POST.get("languages")
        mobile_number = request.POST.get("mobile_number")
        email = request.POST.get("email")
        address = request.POST.get("address")
        qualification = request.POST.get("qualification")
        experience = request.POST.get("experience")
        skills = request.POST.get("skills")
        last_education = request.POST.get("last_education")
        education_name = request.POST.get("education_name")
        education_year = request.POST.get("education_year")
        education_institute = request.POST.get("education_institute")
        Position = request.POST.get("Position")
        Company_name = request.POST.get("Company_name")
        Duration = request.POST.get("Duration")
        company_name = request.POST.get("company_name")
        company_location = request.POST.get("company_location")
        recruiter_name = request.POST.get("recruiter_name")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        current_user = request.user
        if password == cpassword:
            if check_password(cpassword,current_user.password):
                current_user.profile_photo = profile_photo
                current_user.first_name = first_name
                current_user.last_name = last_name
                current_user.age = age
                current_user.gender = gender
                current_user.country = country
                current_user.bloodGroup = bloodGroup
                current_user.save()
                current_user.basicinfomodel.father_name = father_name
                current_user.basicinfomodel.mother_name = mother_name
                current_user.basicinfomodel.hobby = hobby
                current_user.basicinfomodel.languages = languages
                current_user.basicinfomodel.save()
                current_user.contactmodel.mobile_number = mobile_number
                current_user.contactmodel.email = email
                current_user.contactmodel.address = address
                current_user.contactmodel.save()
                if current_user.userType == "seeker":
                    current_user.seekerprofilemodel.Qualification = qualification
                    current_user.seekerprofilemodel.Experience = experience
                    current_user.seekerprofilemodel.Skills = skills
                    current_user.seekerprofilemodel.last_education = last_education
                    current_user.seekerprofilemodel.save()
                    current_user.seekereducationmodel.education_name = education_name
                    current_user.seekereducationmodel.education_year = education_year
                    current_user.seekereducationmodel.education_institute = education_institute
                    current_user.seekereducationmodel.save()
                    current_user.seekerworkexmodel.Position = Position
                    current_user.seekerworkexmodel.Company_name = Company_name
                    current_user.seekerworkexmodel.Duration = Duration
                    current_user.seekerworkexmodel.save()
                elif current_user.userType == "recruiter":
                    current_user.recruiterprofilemodel.Company_name = company_name
                    current_user.recruiterprofilemodel.Company_location = company_location
                    current_user.recruiterprofilemodel.Recruiter_Name = recruiter_name
                    current_user.recruiterprofilemodel.save()
                return redirect('profile')
    return render(request,'editprofile.html')

def addjob(request):
    if request.method == "POST":
        job_title = request.POST.get('job_title')
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        company_description = request.POST.get('company_description')
        company_description = request.POST.get('job_description')
        qualification = request.POST.get('qualification')
        salary_information = request.POST.get('salary_information')
        deadline = request.POST.get('deadline')
        designation = request.POST.get('designation')
        experience = request.POST.get('experience')
        current_user = request.user
        
        job = AddJobModel(
            job_title=job_title,
            company_name=company_name,
            address=address,
            company_description=company_description,
            qualification=qualification,
            salary_information=salary_information,
            deadline=deadline,
            designation=designation,
            experience=experience,
            created_by=current_user,
        )
        job.save()
        return redirect('viewalljob')
    return render(request,'recruiter/addjob.html')

def viewalljob(request):
    job = AddJobModel.objects.all()
    jobDict={
        job:'job'
    }
    return render(request,'viewalljob.html',jobDict)












