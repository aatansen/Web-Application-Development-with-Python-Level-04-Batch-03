from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jobProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name='signup'),
    path('',signin,name='signin'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    
    # job 
    path('addjob/',addjob,name='addjob'),
    path('viewjob/',viewjob,name='viewjob'),
    path('editjob/<str:jobid>',editjob,name='editjob'),
    path('deletejob/<str:jobid>',deletejob,name='deletejob'),
    path('applyjob/<str:jobid>',applyjob,name='applyjob'),
    path('appliedjob/',appliedjob,name='appliedjob'),
    path('applicants/<str:jobid>',applicants,name='applicants'),
    path('jobreject/<str:jobid>',jobreject,name='jobreject'),
    path('jobcallinterview/<str:jobid>',jobcallinterview,name='jobcallinterview'),
    path('callforinterview/',callforinterview,name='callforinterview'),
    path('datefix/',datefix,name='datefix'),
    path('searchpage/',searchpage,name='searchpage'),
    
    
    # profile 
    path('baseprofile/',baseprofile,name='baseprofile'),
    path('profileinfo/',profileinfo,name='profileinfo'),
    path('basicprofile/',basicprofile,name='basicprofile'),
    path('recruitercontact/',recruitercontact,name='recruitercontact'),
    path('seekereducation/',seekereducation,name='seekereducation'),
    path('seekerwork/',seekerwork,name='seekerwork'),
    path('changepassword/',changepassword,name='changepassword'),
    path('specificjobpost/',specificjobpost,name='specificjobpost'),
    path('editprofile/',editprofile,name='editprofile'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
