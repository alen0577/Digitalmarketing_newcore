from django.shortcuts import render,redirect
from Registration_Login.models import *
from .models import *
from DM_Head.models import *
from django.utils import timezone
from datetime import date
from datetime import datetime, timedelta
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
        notification=Notification.objects.filter(emp_id=dash_details,notific_status=0)
        
        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications,
            'notification':notification,
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
        notification=Notification.objects.filter(emp_id=dash_details,notific_status=0)
        
        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications,
            'notification':notification,
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
        notification=Notification.objects.filter(emp_id=dash_details,notific_status=0)


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
                'notification':notification,
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
                'notification':notification,
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
        notification=Notification.objects.filter(emp_id=dash_details,notific_status=0)
        
        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications,
            'notification':notification,
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
        notification=Notification.objects.filter(emp_id=dash_details,notific_status=0)

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
                'notification':notification,
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
                'notification':notification,
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
        notification=Notification.objects.filter(emp_id=dash_details,notific_status=0)
        id1=EmployeeRegister_Details.objects.get(logreg_id=emp_id)
        actions=ActionTaken.objects.filter(act_emp_id=id1).order_by('-action_date')
        

        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications,
            'notification':notification,
            'actions':actions,
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
        notification=Notification.objects.filter(emp_id=dash_details,notific_status=0)
        

        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications,
            'notification':notification,
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
        notification=Notification.objects.filter(emp_id=dash_details,notific_status=0)

        employee_ids = [1, 2]
        employees=EmployeeRegister_Details.objects.filter(emp_designation_id__in=employee_ids)
        id1=EmployeeRegister_Details.objects.get(logreg_id=emp_id).id
        feedback_view=Feedback.objects.filter(from_id=id1).order_by('-feedback_date')

        

        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications,
            'notification':notification,
            'employees':employees,
            'feedback_view':feedback_view
        }

        return render(request,'Executive_feedback.html',content)

    else:
        return redirect('/')

def exadd_feedback(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        notification=Notification.objects.filter(emp_id=dash_details,notific_status=0)

        employee_ids = [1, 2]
        employees=EmployeeRegister_Details.objects.filter(emp_designation_id__in=employee_ids)
        id1=EmployeeRegister_Details.objects.get(logreg_id=emp_id)
        id2=EmployeeRegister_Details.objects.get(logreg_id=emp_id).id
        feedback_view=Feedback.objects.filter(from_id=id2).order_by('-feedback_date')

        if request.POST:
            from_id=id1.id
            from_name=id1.emp_name
            feedback_date=date.today()
            idto=request.POST['feedbackto']
            feedback_emp_id=EmployeeRegister_Details.objects.get(id=idto)
            feedback_content=request.POST['feedback_content']
            feedback=Feedback(from_id=from_id,from_name=from_name,feedback_date=feedback_date,feedback_emp_id=feedback_emp_id,feedback_content=feedback_content)
            feedback.save()
            success_text = 'Feedback Submitted'
            success = True
            content = {
                'emp_dash':emp_dash,
                'dash_details':dash_details,
                'notifications':notifications,
                'notification':notification,
                'employees':employees,
                'feedback_view':feedback_view,
                'success_text':success_text,
                'success':success,
            }
        else:

            error=True
            error_text = 'Oops! something went wrong.'
            content = {
                'emp_dash':emp_dash,
                'dash_details':dash_details,
                'notifications':notifications,
                'notification':notification,
                'employees':employees,
                'feedback_view':feedback_view,
                'error':error,
                'error_text':error_text,
                
            }      

        

        

        return render(request,'Executive_feedback.html',content)

    else:
        return redirect('/')


# feedbackgiven filter 

def exfeedback_given(request):
    
    if request.session.has_key('emp_id'):
        emp_id = request.session['emp_id']
        
    else:
        return redirect('/')

    id1=EmployeeRegister_Details.objects.get(logreg_id=emp_id).id
    feedback_view =Feedback.objects.filter(from_id=id1).order_by('-feedback_date')
    feedback_list=[]

    for i in feedback_view:
        date=i.feedback_date
        by=i.from_name
        byid=i.from_id
        content=i.feedback_content
        to=i.feedback_emp_id.emp_name
        feedback_list.append({
            'feedback_date':date,
            'from_name':by,
            'from_id':byid,
            'feedback_content':content,
            'feedback_emp':to
        })

    return JsonResponse({'feedback_list': feedback_list})   


# feedbackreceived filter 

def exfeedback_received(request):
    
    if request.session.has_key('emp_id'):
        emp_id = request.session['emp_id']
        
    else:
        return redirect('/')
        
    id1=EmployeeRegister_Details.objects.get(logreg_id=emp_id).id
    feedback_view = Feedback.objects.filter(feedback_emp_id=id1).order_by('-feedback_date')
    feedback_list=[]
    for i in feedback_view:
        date=i.feedback_date
        by=i.from_name
        byid=i.from_id
        content=i.feedback_content
        to=i.feedback_emp_id.emp_name
        feedback_list.append({
            'feedback_date':date,
            'from_name':by,
            'from_id':byid,
            'feedback_content':content,
            'feedback_emp':to
        })

    return JsonResponse({'feedback_list': feedback_list})   


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
        notification=Notification.objects.filter(emp_id=dash_details,notific_status=0)

        id1=EmployeeRegister_Details.objects.get(logreg_id=emp_id)
        view_complaints=Complaints.objects.filter(complaint_emp_id=id1).order_by('-complaint_date')
        

        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications,
            'notification':notification,
            'view_complaints':view_complaints,
        }

        return render(request,'Executive_complaints.html',content)

    else:
            return redirect('/')

def addex_complaint(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
        
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        notification=Notification.objects.filter(emp_id=dash_details,notific_status=0)

        id1=EmployeeRegister_Details.objects.get(logreg_id=emp_id)
        view_complaints=Complaints.objects.filter(complaint_emp_id=id1).order_by('-complaint_date')

        if request.POST:
            compaint_head=request.POST['compaint_head']
            compaint_content=request.POST['compaint_content']
            complaint_date=date.today()

            complaint=Complaints(complaint_emp_id=id1, compaint_head= compaint_head,compaint_content=compaint_content,complaint_date=complaint_date)
            complaint.save()
            success_text = 'Complaint Registered'
            success = True
            content = {
                'emp_dash':emp_dash,
                'dash_details':dash_details,
                'notifications':notifications,
                'notification':notification,
                'success_text':success_text,
                'success':success,
                'view_complaints':view_complaints,
                
            }
        else:

            error=True
            error_text = 'Oops! something went wrong.'
            content = {
                'emp_dash':emp_dash,
                'dash_details':dash_details,
                'notifications':notifications,
                'notification':notification,
                'error':error,
                'error_text':error_text,
                'view_complaints':view_complaints
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
        myleave=EmployeeLeave.objects.filter(emp_id=id1).order_by('-leave_apply_date')
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        notification=Notification.objects.filter(emp_id=dash_details,notific_status=0)
        


        

        content = {
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'notifications':notifications,
            'notification':notification,
            'myleave':myleave,
            
            
        }

        return render(request,'Executive_leave.html',content)

    else:
        return redirect('/')

# function to find number of days

def count_weekdays(start_date, end_date):
    current_date = start_date
    weekdays_count = 0

    # Iterate through each date within the range
    while current_date <= end_date:
        # Check if the current date is a weekday (Monday to Saturday)
        if current_date.weekday() < 6 and current_date.weekday() != 6:
            weekdays_count += 1
        
        # Move to the next day
        current_date += timedelta(days=1)

    return weekdays_count


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
        notification=Notification.objects.filter(emp_id=dash_details,notific_status=0)

        id1=EmployeeRegister_Details.objects.get(logreg_id=emp_id)
        myleave=EmployeeLeave.objects.filter(emp_id=id1).order_by('-leave_apply_date')

        # fetch leave details
        if request.POST:
            start_date=request.POST['from']
            end_date=request.POST['to']
            leave_type=request.POST['type_select']
            leave_reason=request.POST['reason']
            leave_apply_date=date.today()

            leave_details=EmployeeLeave(emp_id=id1,start_date=start_date,end_date=end_date,leave_type=leave_type,leave_reason=leave_reason,leave_apply_date=leave_apply_date)
            leave_details.save()

            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            # Calculate the difference in days
            weekdays_count = (count_weekdays(start_date, end_date))
            leave_details.no_of_days = weekdays_count
            leave_details.save()

            success_text = 'Applied Leave'
            success = True
            content = {
                'emp_dash':emp_dash,
                'dash_details':dash_details,
                'notifications':notifications,
                'notification':notification,
                'success_text':success_text,
                'success':success,
                'myleave':myleave,
            }

            # return redirect('executive_leave')
        else:

            error=True
            error_text = 'Oops! something went wrong.'
            content = {
                'emp_dash':emp_dash,
                'dash_details':dash_details,
                'notifications':notifications,
                'notification':notification,
                'error':error,
                'error_text':error_text,
                'myleave':myleave,
            }    


        

        return render(request,'Executive_leave.html',content)

    else:
        return redirect('/')


# leave filter function

def filter_exleave(request):
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    if request.session.has_key('emp_id'):
        emp_id = request.session['emp_id']
    id1=EmployeeRegister_Details.objects.get(logreg_id=emp_id)
    myleave = list(EmployeeLeave.objects.filter(start_date__range=[from_date, to_date],emp_id=id1,).values())

    return JsonResponse({'myleave': myleave})       





# logout

def executive_logout(request):
    request.session.pop('emp_id', None)
    return redirect('login_page')            