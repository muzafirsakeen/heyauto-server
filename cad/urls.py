
from django.contrib import admin
from django.urls import path,include
from django.conf import settings  
from django.conf.urls.static import static 

urlpatterns = [
    path('',include('mainpage.urls')),
    path("admins/", admin.site.urls),
    path('admin/', include('customadmin.urls')),
    path('apis/', include('apis.urls'))  

]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
