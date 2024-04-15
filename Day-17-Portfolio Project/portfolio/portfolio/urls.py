from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import portfolio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',portfolio,name='portfolio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
