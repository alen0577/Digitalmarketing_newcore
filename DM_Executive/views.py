from django.shortcuts import render,redirect
from Registration_Login.models import *
from .models import *
from DM_Head.models import *
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
        
        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications
        }

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
        
        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications
        }

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
        
        
            content = {
                'emp_dash':emp_dash,
                'dash_details':dash_details,
                'notifications':notifications,
                'success_text':success_text,
                'success':success
            }

        else:
            error_text = 'Profile Details Updated.'
            error = True
            content = {
                'emp_dash':emp_dash,
                'dash_details':dash_details,
                'notifications':notifications,
                'error_text':error_text,
                'error':error
            }

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


# Password Section -----------------------------------

def executive_password(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        
        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications
        }

        return render(request,'Executive_password.html',content)

    else:
            return redirect('/')


def user_passwordUpdate(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)

        if request.POST:
           
           emp_dash.log_username = request.POST['emp_uname']
           emp_dash.log_password = request.POST['emp_password']

           emp_dash.save()  
           success = True
           success_text = 'User name or password change.'
        
           content = {
                'emp_dash':emp_dash,
                'dash_details':dash_details,
                'notifications':notifications,
                'success':success,
                'success_text':success_text
            }
        else:

            error=True
            error_text = 'Oops! something went wrong.'
            content = {
                'emp_dash':emp_dash,
                'dash_details':dash_details,
                'notifications':notifications,
                'error':error,
                'error_text':error_text
            }

        return render(request,'Executive_password.html',content)

    else:
            return redirect('/')


# Action Taken -------------------

def executive_actionTaken(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        

        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications
        }

        return render(request,'Executive_actionTaken.html',content)

    else:
            return redirect('/')
     


# Notifications section

def executive_allnotification(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):

            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        

        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications
        }

        return render(request,'Executive_allnotification.html',content)

    else:
            return redirect('/')


# Feedback -------------------------

def executive_feedback(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        

        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications
        }

        return render(request,'Executive_feedback.html',content)

    else:
        return redirect('/')


# Complaints ---------------------

def executive_complaints(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        

        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications
        }

        return render(request,'Executive_complaints.html',content)

    else:
            return redirect('/')
    


# Leave ------------------------------

def executive_leave(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        id1=EmployeeRegister_Details.objects.get(logreg_id=emp_id)
        myleave=EmployeeLeave.objects.filter(emp_id=id1)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)


        

        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications,
            'myleave':myleave,
        }

        return render(request,'Executive_leave.html',content)

    else:
        return redirect('/')
    

def exapply_leave(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        id1=EmployeeRegister_Details.objects.get(logreg_id=emp_id)

        # fetch leave details
        if request.POST:
            start_date=request.POST['from']
            end_date=request.POST['to']
            leave_type=request.POST['type_select']
            leave_reason=request.POST['reason']
            leave_apply_date=date.today()

            leave_details=EmployeeLeave(emp_id=id1,start_date=start_date,end_date=end_date,leave_type=leave_type,leave_reason=leave_reason,leave_apply_date=leave_apply_date)
            leave_details.save()
            return redirect('executive_leave')


        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications
        }

        return render(request,'Executive_leave.html',content)

    else:
        return redirect('/')


def executive_logout(request):
    request.session.pop('emp_id', None)
    return redirect('login_page')            