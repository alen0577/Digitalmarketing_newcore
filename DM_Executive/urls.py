from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   
    # Executive Module --------------------------------

    path('Executive-Dashboard',views.executive_dashboard,name='executive_dashboard'),
    path('Executive-Logout',views.executive_logout,name='executive_logout'),

    # Profile ------------------------------

    path('Executive_Profile',views.executive_profile,name='executive_profile'),
    path('Profile-Update',views.Profile_detailsUpdate,name='Profile_detailsUpdate'),
    path('Profile-Image\Remove',views.profileImage_remove,name='profileImage_remove'),



    
    

    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)