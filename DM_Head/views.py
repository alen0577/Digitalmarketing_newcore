from django.shortcuts import render,redirect
from Registration_Login.models import *
from .models import *
from django.utils import timezone
from datetime import date
from django.http import JsonResponse



def head_dashboard(request):
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

        return render(request,'HD_dashboard.html',content)

    else:
            return redirect('/')



# Profile Page -------------------------
def head_profile(request):  
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

        return render(request,'HD_profile.html',content)

    else:
            return redirect('/')
    

    
def profile_detailsUpdate(request):
     
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

        return render(request,'HD_profile.html',content)

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

def head_password(request):
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

        return render(request,'HD_password.html',content)

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
        
           content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'success':success,
                   'success_text':success_text}
        else:

            error=True
            error_text = 'Oops! something went wrong.'
            content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'error':error,
                    'error_text':error_text}

        return render(request,'HD_password.html',content)

    else:
            return redirect('/')


#Schedule -------------------------------------------

def head_schedule(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
          
        today = date.today()
        schedules = EmployeeSchedule.objects.filter(emp_id=dash_details)
        schedule_days = EmployeeSchedule.objects.filter(emp_id=dash_details, schedule_date=today).values('schedule_date').distinct()

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'schedules':schedules,
                   'schedule_days':schedule_days}

        return render(request,'HD_dayTaskschedule.html',content)

    else:
            return redirect('/')
    
    
def head_scheduleRemove(request,pk):
     
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)

        schedule_remove = EmployeeSchedule.objects.get(id=pk)
        schedule_remove.delete()  

        error = True
        error_text = 'Schedule task removed'
        
        today = date.today()
        schedules = EmployeeSchedule.objects.filter(emp_id=dash_details)
        schedule_days = EmployeeSchedule.objects.filter(emp_id=dash_details, schedule_date=today).values('schedule_date').distinct()

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'schedules':schedules,
                   'schedule_days':schedule_days,'error':error,'error_text':error_text}

        return render(request,'HD_dayTaskschedule.html',content)

    else:
            return redirect('/')
    

def head_schedule_save(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        
        schedules = None
        schedule_days = None

        if request.POST:

            if request.POST['scheduleId']:

                schedule_obj = EmployeeSchedule.objects.get(id=int(request.POST['scheduleId']))

                schedule_obj.emp_id=dash_details
                schedule_obj.start_time=request.POST['stime']
                schedule_obj.end_time=request.POST['etime']
                schedule_obj.schedule_head=request.POST['task_head']
                schedule_obj.todo_content=request.POST['task_content']
                schedule_obj.log_time = timezone.now()
                schedule_obj.schedule_date = date.today()
                schedule_obj.save()

                today = date.today()
                schedules = EmployeeSchedule.objects.filter(emp_id=dash_details)
                schedule_days = EmployeeSchedule.objects.filter(emp_id=dash_details, schedule_date=today).values('schedule_date').distinct()
                success_text = 'Schedule edit successful.'
                success = True

            else:

    
                schedule_obj = EmployeeSchedule()

                schedule_obj.emp_id=dash_details
                schedule_obj.start_time=request.POST['stime']
                schedule_obj.end_time=request.POST['etime']
                schedule_obj.schedule_head=request.POST['task_head']
                schedule_obj.todo_content=request.POST['task_content']
                schedule_obj.log_time = timezone.now()
                schedule_obj.schedule_date = date.today()

                schedule_obj.save()

                today = date.today()
                schedules = EmployeeSchedule.objects.filter(emp_id=dash_details)
                schedule_days = EmployeeSchedule.objects.filter(emp_id=dash_details, schedule_date=today).values('schedule_date').distinct()

                success_text = 'Schedule save successful.'
                success = True

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'success_text':success_text,
                   'success':success,
                   'schedules':schedules,
                   'schedule_days':schedule_days}

        return render(request,'HD_dayTaskschedule.html',content)

    else:
            return redirect('/')


def ScheduleEdit(request):

    schedule_id = request.GET.get('scheduleid')
    try:
            schedule = EmployeeSchedule.objects.get(id=schedule_id)
           
            data = {
                'scheduleid':schedule.id,
                'start_time': schedule.start_time,
                'end_time': schedule.end_time,
                'task_head': schedule.schedule_head,
                'task_content': schedule.todo_content,
            }
            return JsonResponse(data)
    except EmployeeSchedule.DoesNotExist:
            return JsonResponse({'error': 'Schedule not found'}, status=404)  


def update_schedule_status(request):
        schedule_id = request.POST.get('schedule_id')
        checked = request.POST.get('checked')

        # Retrieve the schedule by ID
        schedule = EmployeeSchedule.objects.get(id=schedule_id)
        if schedule.schedule_status == 0:
            schedule.schedule_status =  1
        else: 
            schedule.schedule_status =  0
        schedule.save()
        return JsonResponse({'success': True})


def head_employees_schedule(request):

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

        return render(request,'HD_employees_dayTaskschedule.html',content)

    else:
            return redirect('/')
     

def head_scheduleFilter(request):

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

        return render(request,'HD_scheduleFilter.html',content)

    else:
            return redirect('/')
     

# Feedback -------------------------

def head_feedback(request):

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

        return render(request,'HD_feedback.html',content)

    else:
            return redirect('/')
     
     

# Complaints ---------------------

def head_complaints(request):
    
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

        return render(request,'HD_complaints.html',content)

    else:
            return redirect('/')
     

# Action Taken -------------------

def head_actionTaken(request):
    
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

        return render(request,'HD_actionTaken.html',content)

    else:
            return redirect('/')
     

# Leave ------------------------------


def head_leave(request):
    
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

        return render(request,'HD_leave.html',content)

    else:
            return redirect('/')
    

# Notification -----------------------


def head_allnotification(request):
    
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

        return render(request,'HD_allnotification.html',content)

    else:
            return redirect('/')


def head_logout(request):
    request.session.pop('emp_id', None)
    return redirect('login_page')
