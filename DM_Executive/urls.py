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
    path('Exprofile-Update',views.Profile_detailsUpdate,name='Profile_detailsUpdate'),
    path('Exprofile-Image\Remove',views.profileImage_remove,name='profileImage_remove'),


    # Password ----------------------------

    path('Expassword',views.executive_password,name='executive_password'),
    path('Expassword-Update',views.user_passwordUpdate,name='user_passwordUpdate'),


    # Action Taken  --------------------------

    path('Executive-Action-Taken',views.executive_actionTaken,name='executive_actionTaken'),

    
    # Notification ----------------------

    path('Executive-Notification',views.executive_allnotification,name='executive_allnotification'),


    # Feedback  --------------------------

    path('Executive-Feedback',views.executive_feedback,name='executive_feedback'),
    path('Executive-Add-Feedback',views.exadd_feedback,name='exadd_feedback'),
    path('Executive-Feedbackgiven',views.exfeedback_given,name='exfeedback_given'),
    path('Executive-Feedbackreceived',views.exfeedback_received,name='exfeedback_received'),


    # Complaints --------------------------

    path('Executive-Complaints',views.executive_complaints,name='executive_complaints'),
    path('Add-Executive-Complaints',views.addex_complaint,name='addex_complaint'),

    # Leave ---------------------------
    
    path('Executive-Leave',views.executive_leave,name='executive_leave'),
    path('Exapply-leave',views.exapply_leave,name='exapply_leave'),
    path('Filterex-Leave',views.filter_exleave,name='filter_exleave'),



]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)