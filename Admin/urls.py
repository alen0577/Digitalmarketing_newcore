from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   
    #  Admin Module --------------------------------

    path('Admin-Dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('Admin-Logout',views.admin_logout,name='admin_logout'),

    # Department ---------------------------------
    
    path('Admin-Department',views.admin_department,name='admin_department'),

    # Designation -------------------------------

    path('Admin-Designations',views.admin_designation,name='admin_designation'),

    # Employees Section -----------------

    path('Admin-Employees-Section',views.admin_employees_section,name='admin_employees_section'),
    path('Admin-Employees-View',views.admin_viewEmployees,name='admin_viewEmployees'),
    path('Admin-Employees-Resigned',views.admin_resignedEmployees,name='admin_resignedEmployees'),
    path('Admin-Employees-Leaves',views.admin_Employeesleaves,name='admin_Employeesleaves'),
    path('Admin-Employee-leaveDetails',views.admin_get_employee_details,name='admin_get_employee_details'),
    # path('Employees-Allocate',views.head_employeeAllocate,name='head_employeeAllocate'),
    # path('Employees-Allocate-List',views.head_employeeAllocated_list,name='head_employeeAllocated_list'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)