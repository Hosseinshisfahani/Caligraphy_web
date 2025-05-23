from django.conf import settings  
from django.conf.urls.static import static  
from django.contrib import admin  
from django.urls import path, include  
from django.contrib.auth import views as auth_views  


urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', include('calligraphyApp.urls')),  # Include the URLs from calligraphyApp  
    path('login/', auth_views.LoginView.as_view(), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Optional, for logout  
]  


if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  