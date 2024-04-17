from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import portfolio,editabout,updateabout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',portfolio,name='portfolio'),
    path('editabout/<str:myid>',editabout,name='editabout'),
    path('updateabout/',updateabout,name='updateabout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
