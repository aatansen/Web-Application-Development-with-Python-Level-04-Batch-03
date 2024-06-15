from django.shortcuts import render,redirect
from schoolApp.models import *

def sessionadd(request):
    if request.method=="POST":
        Session_Year=request.POST.get('Session_Year')
        session=SessionAddModel.objects.create(
            Session_Year=Session_Year
        )
        session.save()
        return redirect('sessionlist')
        
    return render(request,'sessions/sessionadd.html')

def sessionlist(request):
    session=SessionAddModel.objects.all()
    session_list=[]
    
    for i in session:
        student_count=StudentAddModel.objects.filter(mySessionYear=i).count()
        
        session_list.append(
            {
                'id':i.id,
                'student_count':student_count,
                'Session_Year':i.Session_Year,
            }
        )
        
    
    sessionDict={
        'session_list':session_list,
    }
    
    return render(request,'sessions/sessionlist.html',sessionDict)

def sessiondelete(request,sessionid):
    session=SessionAddModel.objects.get(id=sessionid)
    session.delete()
    return redirect('sessionlist')