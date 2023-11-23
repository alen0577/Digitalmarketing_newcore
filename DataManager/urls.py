from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   
    # Data Manager Module --------------------------------

    path('Data-Manager-Dashboard',views.dataManager_dashboard,name='dataManager_dashboard'),

    # Data Manager Account section --------------------------------

    path('Data-Manager/Password-Section',views.DAM_password,name='DAM_password'),
    path('Data-Manager/Password-change',views.DAM_passwordUpdate,name='DAM_passwordUpdate'),

    path('Data-Manager/Profile',views.DAM_profile,name='DAM_profile'),
    path('Data-Manager/Update-Profile',views.DAM_profile_detailsUpdate,name='DAM_profile_detailsUpdate'),


    #Side Navbar --------------------------
    path('Data-Manager-HR-Telecaller/',views.DAM_employees_hr_tel,name='DAM_employees_hr_tel'),
    path('Data-Manager-Executive/',views.DAM_employees_exe,name='DAM_employees_exe'),
    path('Data-Manager-Details-Employees/<int:empDeatilsID>',views.DAM_employess_details,name='DAM_employess_details'),
    

    # Data Manager Notification Section ----------------

    path('Notification-Management',views.DAM_notification_section,name='DAM_notification_section'),


    # Data Manager Executive Dashboard Section ---------

    path('Executive-Dashboard-Management/',views.DAM_executive_dashboard,name='DAM_executive_dashboard'),
    path('Clients-New-Leads/',views.DAM_client_newleads,name='DAM_client_newleads'),
    path('Clients/New-Leads-List/<int:clID>',views.DAM_client_lists_newLeads,name='DAM_client_lists_newLeads'),
    path('Executives/',views.DAM_executive_lead,name='DAM_executive_lead'),
    path('Executive-All/Leads-List/<int:eID>',views.DAM_executive_collected_leads,name='DAM_executive_collected_leads'),
    path('Clients-All-Leads/',views.DAM_all_clientleads,name='DAM_all_clientleads'),
    path('Clients-All/Leads-List/<int:cID>',views.DAM_client_lists_allLeads,name='DAM_client_lists_allLeads'),

    # Data Manager Allocation dashboard Section -----------------------

    
    path('Allocation-Dashboard-Management/',views.DAM_allocation_dashboard,name='DAM_allocation_dashboard'),
    path('Allocation-Pending/',views.DAM_pendingleads,name='DAM_pendingleads'),
    path('Allocated-Lead/',views.DAM_allocated_leads,name='DAM_allocated_leads'),
    path('Client-Allocation-Pending/<int:cID>',views.DAM_client_pendingLeads,name='DAM_client_pendingLeads'),
    path('Client-Category-Pending/<int:lCID>',views.DAM_client_category_pendingLeads,name='DAM_client_category_pendingLeads'),
    path('Allocation/',views.DMA_allocate_lead,name='DMA_allocate_lead'),
    
    
    


    # Data Manager Telecaller Dashboard Section -------

    path('Telecaller-Dashboard-Management/',views.DAM_telecallers_dashboard,name='DAM_telecallers_dashboard'),


    # Data Manager platform  Section -------

    path('Platform-Management/',views.DAM_platform_management,name='DAM_platform_management'),
    path('Add-Platform',views.DAM_platform_add,name='DAM_platform_add'),
    path('Platform-Leads/<int:pID>',views.DAM_platform_leads,name='DAM_platform_leads'),


    # Data Manager Telecaller Dashboard Section -------

    path('WasteData-Management/',views.DAM_wasteData_management,name='DAM_wasteData_management'),
    
    
    path('DataManager-Logout/',views.DAM_logout,name='DAM_logout'),

    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)