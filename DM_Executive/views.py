from django.shortcuts import render,redirect
from Registration_Login.models import *
from .models import *
from django.utils import timezone
from datetime import date
from django.http import JsonResponse

# Create your views here.

def executive_dashboard(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'Executive_dashboard.html',content)

    else:
            return redirect('/')


# Profile Page -------------------------
def executive_profile(request):  
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'Executive_profile.html',content)

    else:
            return redirect('/')


def Profile_detailsUpdate(request):
     
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)


        # Details Save -----------------

        if request.POST:
             
             emp_obj = EmployeeRegister_Details.objects.get(id=dash_details.id)

             emp_obj.emp_name = request.POST['empname']
             emp_obj.emp_contact_no = request.POST['contactno']
             emp_obj.emp_email = request.POST['empEmail']
             emp_obj.emp_address1 = request.POST['add1']
             emp_obj.emp_address2 = request.POST['add2']
             emp_obj.emp_address3 = request.POST['add3']
             emp_obj.emp_pin = request.POST['pincode']
             emp_obj.emp_location = request.POST['loc']
             emp_obj.emp_district = request.POST['empdist']
             emp_obj.emp_state = request.POST['empState']

             if request.FILES.get('empProfile'):
                emp_obj.emp_profile = request.FILES.get('empProfile')

             else:
                emp_obj.emp_profile =  emp_obj.emp_profile 

             if request.FILES.get('empResume'):
                emp_obj.emp_file = request.FILES.get('empResume')

             else:
                emp_obj.emp_file =  emp_obj.emp_file 

             emp_obj.save()
             success_text = 'Profile Details Updated.'
             success = True

             dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        
             content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'success_text':success_text,
                    'success':success}

        else:
            error_text = 'Profile Details Updated.'
            error = True
            content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'error_text':error_text,
                    'error':error}

        return render(request,'Executive_profile.html',content)

    else:
            return redirect('/')
    

# Remove Profile Image ---------------

def profileImage_remove(request):
    emp_id = request.POST.get('emp_id')
    dash_details = EmployeeRegister_Details.objects.get(id=emp_id)
    dash_details.emp_profile = ''
    dash_details.save()
    return JsonResponse({'message': 'Received emp_id: ' + emp_id})
     
# End ------------------------------------------------



def executive_logout(request):
    request.session.pop('emp_id', None)
    return redirect('login_page')            