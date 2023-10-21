from django.shortcuts import render,redirect
from Registration_Login.models import *
from django.db.models import Q
from DM_Head.models import *
from django.http import JsonResponse



def admin_dashboard(request):
    if 'admin_id' in request.session:
        if request.session.has_key('admin_id'):
            admin_id = request.session['admin_id']
           
        else:
            return redirect('/')
        
        Admin_dash = LogRegister_Details.objects.get(id=admin_id)
        dash_details = BusinessRegister_Details.objects.get(log_id=Admin_dash)
        
        content = {'Admin_dash':Admin_dash,'dash_details':dash_details}

        return render(request,'AD_dashboard.html',content)

    else:
            return redirect('/')
    


# Department ---------------------

def admin_department(request):
    if 'admin_id' in request.session:
        if request.session.has_key('admin_id'):
            admin_id = request.session['admin_id']
           
        else:
            return redirect('/')
        
        Admin_dash = LogRegister_Details.objects.get(id=admin_id)
        dash_details = BusinessRegister_Details.objects.get(log_id=Admin_dash)
        departments = DepartmentRegister_details.objects.filter(brd_id=dash_details)

        if request.POST:
             
            depart_obj = DepartmentRegister_details()
            depart_obj.dept_name = request.POST['department_name']
            depart_obj.dept_content = request.POST['department_discription']
            depart_obj.dept_active_status = 1
            depart_obj.brd_id = dash_details
            depart_obj.save()

            success = True
            success_text = 'New department created successfully '

            departments = DepartmentRegister_details.objects.filter(brd_id=dash_details)

        
            content = {'Admin_dash':Admin_dash,
                   'dash_details':dash_details,
                   'success':success,
                   'success_text':success_text,
                   'departments':departments}
        else:
             
            content = {'Admin_dash':Admin_dash,
                   'dash_details':dash_details,
                    'departments':departments}

        return render(request,'AD_department.html',content)

    else:
            return redirect('/')
    


# Designation ----------------------------

def admin_designation(request):
    if 'admin_id' in request.session:
        if request.session.has_key('admin_id'):
            admin_id = request.session['admin_id']
           
        else:
            return redirect('/')
        
        Admin_dash = LogRegister_Details.objects.get(id=admin_id)
        dash_details = BusinessRegister_Details.objects.get(log_id=Admin_dash)

        departments = DepartmentRegister_details.objects.filter(brd_id=dash_details,dept_active_status=1)
        designations = DesignationRegister_details.objects.filter(dept_id__in=departments)

        if request.POST:
            
            desidnation_obj = DesignationRegister_details()

            desidnation_obj.desig_name = request.POST['designation_name']
            desidnation_obj.desig_content = request.POST['designation_discription']
            desidnation_obj.desig_brd_id = dash_details
            desidnation_obj.dept_id =  DepartmentRegister_details.objects.get(id=int(request.POST['deparmentId'])) 
            desidnation_obj.desig_active_status = 1
            desidnation_obj.dashboard_id = request.POST['dashboardId'] 
            desidnation_obj.save()

            success = True
            success_text = 'New designation add successfully '
            designations = DesignationRegister_details.objects.filter(dept_id__in=departments)

            content = {'Admin_dash':Admin_dash,
                   'dash_details':dash_details,
                   'departments':departments,
                   'designations':designations,
                   'success':success,
                   'success_text':success_text
                   }

        else:
            
            content = {'Admin_dash':Admin_dash,
                   'dash_details':dash_details,
                   'departments':departments,
                   'designations':designations
                   }

        return render(request,'AD_designation.html',content)

    else:
            return redirect('/')
     



# Employees Section ---------------------------------


def admin_employees_section(request):
    if 'admin_id' in request.session:
        if request.session.has_key('admin_id'):
            admin_id = request.session['admin_id']
           
        else:
            
            return redirect('/')
        
        admin_dash = LogRegister_Details.objects.get(id=admin_id)
        dash_details = BusinessRegister_Details.objects.get(log_id=admin_dash)

        # Notification-----------
        
        content = {

            'admin_dash':admin_dash,
            'dash_details':dash_details,
        }

        return render(request,'AD_employeeSection.html',content)

    else:
            return redirect('/')



def admin_viewEmployees(request):
    if 'admin_id' in request.session:
        if request.session.has_key('admin_id'):
            admin_id = request.session['admin_id']
           
        else:
            return redirect('/')
        
        admin_dash = LogRegister_Details.objects.get(id=admin_id)
        dash_details = BusinessRegister_Details.objects.get(log_id=admin_dash)

        # Notification-----------

        employees = EmployeeRegister_Details.objects.filter(Q(emp_comp_id=dash_details, emp_active_status=0) | Q(emp_comp_id=dash_details, emp_active_status=1))
        
        content = {
            'admin_dash':admin_dash,
            'dash_details':dash_details,
            'employees':employees
        }
        
        
        # else:
        #     return render(request,'error-404.html')  

        return render(request,'AD_employeeView.html',content)

    else:
            return redirect('/')    


def admin_resignedEmployees(request):
    if 'admin_id' in request.session:
        if request.session.has_key('admin_id'):
            admin_id = request.session['admin_id']
           
        else:
            return redirect('/')
        
        admin_dash = LogRegister_Details.objects.get(id=admin_id)
        dash_details = BusinessRegister_Details.objects.get(log_id=admin_dash)

        # Notification-----------

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=dash_details,emp_active_status=2)
        
        content = {
            'admin_dash':admin_dash,
            'dash_details':dash_details,
            'employees':employees
        }
        

        return render(request,'AD_employeeresignView.html',content)

    else:
            return redirect('/')    


def admin_Employeesleaves(request):
    if 'admin_id' in request.session:
        if request.session.has_key('admin_id'):
            admin_id = request.session['admin_id']
           
        else:
            return redirect('/')
        
        admin_dash = LogRegister_Details.objects.get(id=admin_id)
        dash_details = BusinessRegister_Details.objects.get(log_id=admin_dash)

        # Notification-----------

        employees = EmployeeRegister_Details.objects.filter(Q(emp_comp_id=dash_details, emp_active_status=0) | Q(emp_comp_id=dash_details, emp_active_status=1))
        
        content = {
            'admin_dash':admin_dash,
            'dash_details':dash_details,
            'employees':employees
        }
        

        return render(request,'AD_employeeLeaves.html',content)

    else:
            return redirect('/')    



def admin_get_employee_details(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        employees = EmployeeRegister_Details.objects.get(id=employee_id)

        # Query your database to fetch employee details based on the employee_id.
        # Replace 'EmployeeLeave' with the actual model that stores employee details.

        employee_details = list(EmployeeLeave.objects.filter(emp_id=employee_id).values())
        print(employee_details)

        # You might want to serialize the 'employee_details' to a JSON format.
        return JsonResponse({'details': employee_details})

    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)








def admin_logout(request):
    request.session.pop('admin_id', None)
    return redirect('login_page')
     


