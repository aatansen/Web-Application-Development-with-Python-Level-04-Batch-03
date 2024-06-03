from django.contrib import admin
from django.urls import path
from myApp.views import StudentApiView,StudentApiView2,StudentUpdateDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentApiView/',StudentApiView,name='StudentApiView'),
    path('StudentApiView2/',StudentApiView2.as_view(),name='StudentApiView2'),
    path('StudentUpdateDelete/<int:pk>',StudentUpdateDelete.as_view(),name='StudentUpdateDelete'),
]
