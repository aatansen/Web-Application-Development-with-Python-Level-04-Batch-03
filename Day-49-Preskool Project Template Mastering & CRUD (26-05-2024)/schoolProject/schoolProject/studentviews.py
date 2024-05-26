from django.shortcuts import render, redirect
from schoolApp.models import StudentAddModel,CustomUserModel

def studentdashboard(request):
    return render(request,'student/studentdashboard.html')

def studentlist(request):
    student=StudentAddModel.objects.all()
    stDict={
        'student':student
    }
    return render(request,'student/studentlist.html',stDict)

def studentadd(request):
    if request.method=="POST":
        First_Name=request.POST.get('First_Name')
        Last_Name=request.POST.get('Last_Name')
        Student_Id=request.POST.get('Student_Id')
        Gender=request.POST.get('Gender')
        Date_of_Birth=request.POST.get('Date_of_Birth')
        Class=request.POST.get('Class')
        Religion=request.POST.get('Religion')
        Joining_Date=request.POST.get('Joining_Date')
        Mobile_Number=request.POST.get('Mobile_Number')
        Admission_Number=request.POST.get('Admission_Number')
        Section=request.POST.get('Section')
        Student_Image=request.FILES.get('Student_Image')
        Father_Name=request.POST.get('Father_Name')
        Father_Occupation=request.POST.get('Father_Occupation')
        Father_Mobile=request.POST.get('Father_Mobile')
        Father_Email=request.POST.get('Father_Email')
        Mother_Name=request.POST.get('Mother_Name')
        Mother_Occupation=request.POST.get('Mother_Occupation')
        Mother_Mobile=request.POST.get('Mother_Mobile')
        Mother_Email=request.POST.get('Mother_Email')
        Present_Address=request.POST.get('Present_Address')
        Permanent_Address=request.POST.get('Permanent_Address')
        Username=request.POST.get('Username')
        Password=request.POST.get('Password')
        CPassword=request.POST.get('CPassword')
        if Password==CPassword:
            student=StudentAddModel.objects.create(
                First_Name=First_Name,
                Last_Name=Last_Name,
                Username=Username,
                Student_Id=Student_Id,
                Gender=Gender,
                Date_of_Birth=Date_of_Birth,
                Class=Class,
                Religion=Religion,
                Joining_Date=Joining_Date,
                Mobile_Number=Mobile_Number,
                Admission_Number=Admission_Number,
                Section=Section,
                Student_Image=Student_Image,
                Father_Name=Father_Name,
                Father_Occupation=Father_Occupation,
                Father_Mobile=Father_Mobile,
                Father_Email=Father_Email,
                Mother_Name=Mother_Name,
                Mother_Occupation=Mother_Occupation,
                Mother_Mobile=Mother_Mobile,
                Mother_Email=Mother_Email,
                Present_Address=Present_Address,
                Permanent_Address=Permanent_Address,
                created_by = request.user
            )
            student.save()
            student_custom=CustomUserModel.objects.create_user(
                username=Username,
                password=Password,
                user_type="3"
            )
            student_custom.save()
            return redirect('studentlist')
    return render(request,'student/studentadd.html')

def studentdetails(request,stuid):
    student_data=StudentAddModel.objects.get(id=stuid)
    stuDict={
        'student_data':student_data
    }
    return render(request,'student/studentdetails.html',stuDict)

def studentedit(request):
    return render(request,'student/studentedit.html')

def studentadelete(request,stuid):
    student_data=StudentAddModel.objects.get(id=stuid)
    student_username=student_data.Username
    student_custom=CustomUserModel.objects.get(username=student_username)
    student_custom.delete()
    student_data.delete()
    return redirect('studentlist')