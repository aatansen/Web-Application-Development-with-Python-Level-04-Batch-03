from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from d17_project.views import student,addstudent,viewstudent,portfolio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('viewstudent/<int:myid>',viewstudent,name='viewstudent'),
    path('portfolio/',portfolio,name='portfolio')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
