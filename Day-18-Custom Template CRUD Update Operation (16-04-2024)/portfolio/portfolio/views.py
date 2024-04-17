from django.shortcuts import redirect,render
from portfolioapp.models import SocialMediaModel,AboutModel,factModel,SkillsModel,SkillMatricesModel,ResumeModel,ResumeEducationModel,ResumeProfessionalModel,PortfolioModel,ServicesModel,ServicesSectionModel,TestimonialModel,ClientTestimonialModel,ContactModel

def portfolio(request):
    socialmedia = SocialMediaModel.objects.get()
    about = AboutModel.objects.get()
    fact = factModel.objects.get()
    skills = SkillsModel.objects.get()
    skills_matrices = SkillMatricesModel.objects.all()
    resume = ResumeModel.objects.get()
    resume_edu = ResumeEducationModel.objects.all()
    resume_pro = ResumeProfessionalModel.objects.all()
    portfolio_des = PortfolioModel.objects.get()
    services_des = ServicesModel.objects.get()
    services_section = ServicesSectionModel.objects.all()
    testimonial_des = TestimonialModel.objects.get()
    client_testimonial = ClientTestimonialModel.objects.all()
    contact = ContactModel.objects.get()
    myDict={
        'socialmedia':socialmedia,
        'about':about,
        'fact':fact,
        'skills':skills,
        'skills_matrices':skills_matrices,
        'resume':resume,
        'resume_edu':resume_edu,
        'resume_pro':resume_pro,
        'portfolio_des':portfolio_des,
        'services_des':services_des,
        'services_section':services_section,
        'testimonial_des':testimonial_des,
        'client_testimonial':client_testimonial,
        'contact':contact,
        
    }
    return render(request,'index.html',myDict)

def editabout(request, myid):
    about = AboutModel.objects.get(id=myid)
    myDict={
        'about':about
    }
    return render(request,'editabout.html',myDict)

def updateabout(request):
    if request.method=="POST":
        myid = request.POST.get('myid')
        profile_img = request.FILES.get('profile_img')
        name=request.POST.get('name')
        profession1=request.POST.get('profession1')
        profession2=request.POST.get('profession2')
        profession3=request.POST.get('profession3')
        about_details=request.POST.get('about_details')
        profession_title1=request.POST.get('profession_title1')
        profession_title2=request.POST.get('profession_title2')
        profession_details=request.POST.get('profession_details')
        profession_para=request.POST.get('profession_para')
        birthday=request.POST.get('birthday')
        website=request.POST.get('website')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        age=request.POST.get('age')
        email=request.POST.get('email')
        freelance_status=request.POST.get('freelance_status')
        if profile_img:  
            about = AboutModel(
                id = myid,
                Profile_img = profile_img,
                Name=name,
                Profession1=profession1,
                Profession2=profession2,
                Profession3=profession3,
                About_details=about_details,
                Profession_title1=profession_title1,
                Profession_title2=profession_title2,
                Profession_details=profession_details,
                Profession_para=profession_para,
                Birthday=birthday,
                Website=website,
                Phone=phone,
                City=city,
                Age=age,
                Email=email,
                Freelance_status=freelance_status,
            )
        else:
            aboutbyid=AboutModel.objects.get(id=myid)
            about = AboutModel(
                id = myid,
                Profile_img = aboutbyid.Profile_img,
                Name=name,
                Profession1=profession1,
                Profession2=profession2,
                Profession3=profession3,
                About_details=about_details,
                Profession_title1=profession_title1,
                Profession_title2=profession_title2,
                Profession_details=profession_details,
                Profession_para=profession_para,
                Birthday=birthday,
                Website=website,
                Phone=phone,
                City=city,
                Age=age,
                Email=email,
                Freelance_status=freelance_status,
            )
        about.save()
        return redirect('/')