from django.contrib import admin
from django.urls import path
from schoolProject.views import signinpage,signuppage,adminpage,teacherdashboard,studentdashboard,studentlist,studentadd,studentedit,studentadelete,teacherlist,teacheradd,studentdetails,teacherdetails,teacheredit,teacherdelete,departmentslist,departmentsadd,departmentsedit,departmentsdelete,subjectslist,subjectsedit,subjectsadd,subjectsdelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signuppage/',signuppage,name='signuppage'),
    path('',signinpage,name='signinpage'),
    path('adminpage/',adminpage,name='adminpage'),
    path('teacherdashboard/',teacherdashboard,name='teacherdashboard'),
    path('studentdashboard/',studentdashboard,name='studentdashboard'),
    path('studentlist/',studentlist,name='studentlist'),
    path('studentadd/',studentadd,name='studentadd'),
    path('studentdetails/',studentdetails,name='studentdetails'),
    path('studentedit/',studentedit,name='studentedit'),
    path('studentadelete/',studentadelete,name='studentadelete'),
    path('teacherlist/',teacherlist,name='teacherlist'),
    path('teacheradd/',teacheradd,name='teacheradd'),
    path('teacherdetails/',teacherdetails,name='teacherdetails'),
    path('teacheredit/',teacheredit,name='teacheredit'),
    path('teacherdelete/',teacherdelete,name='teacherdelete'),
    path('departmentslist/',departmentslist,name='departmentslist'),
    path('departmentsadd/',departmentsadd,name='departmentsadd'),
    path('departmentsedit/',departmentsedit,name='departmentsedit'),
    path('departmentsdelete/',departmentsdelete,name='departmentsdelete'),
    path('subjectslist/',subjectslist,name='subjectslist'),
    path('subjectsadd/',subjectsadd,name='subjectsadd'),
    path('subjectsedit/',subjectsedit,name='subjectsedit'),
    path('subjectsdelete/',subjectsdelete,name='subjectsdelete'),
]
