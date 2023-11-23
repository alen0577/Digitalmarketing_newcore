from django.shortcuts import render,redirect
from DM_Head.models import EmployeeRegister_Details,Notification,Leads,ClientTask_Register,LeadCategory_Register
from Registration_Login.models import LogRegister_Details
from django.db.models import Q
from django.db.models import Count
from .models import *



def dataManager_dashboard(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}
        
    return render(request,'DAM_dashboard.html',content)



#Side Navbar links -------------------------

def DAM_employees_hr_tel(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=dash_details.emp_comp_id,emp_designation_id__dashboard_id=4,emp_active_status=1)
       

       
        content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'employees':employees
                    }
        
    return render(request,'DAM_employees.html',content)


def DAM_employees_exe(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

       
        employees = EmployeeRegister_Details.objects.filter(Q(emp_designation_id__dashboard_id=2) | Q(emp_designation_id__dashboard_id=3),emp_comp_id=dash_details.emp_comp_id,emp_active_status=1)


        content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'employees':employees
                    }
        
    return render(request,'DAM_employees.html',content)


def DAM_employess_details(request,empDeatilsID):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        emp_obj = EmployeeRegister_Details.objects.get(id=empDeatilsID) 

        cid = 2
        
        if emp_obj.emp_designation_id.dashboard_id == 3: 
            
            cid = 0

        if emp_obj.emp_designation_id.dashboard_id == 4 :

            cid = 1

        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'emp_obj':emp_obj,'cid':cid}

        return render(request,'DAM_emp_details.html',content)

    else:
            return redirect('/')


#Password Section ---------------

def DAM_password(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'DAM_password.html',content)

    else:
            return redirect('/')

def DAM_passwordUpdate(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

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

        return render(request,'DAM_password.html',content)

    else:
            return redirect('/')

# Profile Page -------------------------

def DAM_profile(request):  
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'DAM_profile.html',content)

    else:
            return redirect('/')


def DAM_profile_detailsUpdate(request):
     
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')


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

        return render(request,'DAM_profile.html',content)

    else:
            return redirect('/')
    
# ============================================================================


# Data Manager Notification Management Section 

def DAM_notification_section(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}
    return render(request,'DAM_notificationSection.html',content)




# Data Manager Executive Dashboard 

def DAM_executive_dashboard(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}
    return render(request,'DAM_executiveDashboard.html',content)


def DAM_client_newleads(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}
    return render(request,'DAM_clientNew_lead.html',content)

def DAM_client_lists_newLeads(request,clID):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}
    return render(request,'DAM_clientNew_lead_list.html',content)

#---------------------------------------------------------

def DAM_executive_lead(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}
    return render(request,'DAM_executive_lead.html',content)


def DAM_executive_collected_leads(request,eID):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}
    return render(request,'DAM_executive_lead_list.html',content)



#--------------------------------------------------------


def DAM_all_clientleads(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}
    return render(request,'DAM_clientAll_lead.html',content)

def DAM_client_lists_allLeads(request,cID):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}
    return render(request,'DAM_clientAll_lead_list.html',content)


# Data Manager Allocation Dashoard 

def DAM_allocation_dashboard(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        pending_lead = DataBank.objects.filter(lead_Id__lead_collect_Emp_id__emp_comp_id__id=dash_details.emp_comp_id.id,lead_allocate_status=0).count()
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'pending_lead':pending_lead}
    return render(request,'DAM_allocationDashboard.html',content)


def DAM_allocated_leads(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        allocated_lead = DataBank.objects.filter(
                lead_Id__lead_collect_Emp_id__emp_comp_id__id=dash_details.emp_comp_id.id,
                lead_allocate_status=1
            ).values('allocated_date').annotate(count=Count('allocated_date')).order_by('-allocated_date')



        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'allocated_lead':allocated_lead,
                   }
    return render(request,'DAM_allocatedLead.html',content)

    
def DAM_pendingleads(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        clients_obj = ClientTask_Register.objects.filter(cTcompId=dash_details.emp_comp_id,task_name='Lead Collection')
        
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   
                   'clients_obj':clients_obj}
    return render(request,'DAM_allocationPending.html',content)


def DAM_client_pendingLeads(request,cID):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        employees = EmployeeRegister_Details.objects.filter(Q(emp_designation_id__dashboard_id=3) | Q(emp_designation_id__dashboard_id=5))

        lc_obj = LeadCategory_Register.objects.filter(cTaskId__client_Id=cID)

        leads_obj = DataBank.objects.filter(lead_Id__lead_category_id__in=lc_obj,lead_allocate_status=0)

        data_box = {}

        total = DataBank.objects.filter(lead_Id__lead_work_regId__clientId__id=cID).count()
        allocate = DataBank.objects.filter(lead_Id__lead_work_regId__clientId__id=cID,lead_allocate_status=1).count()
        pending = DataBank.objects.filter(lead_Id__lead_work_regId__clientId__id=cID,lead_allocate_status=0).count()

        data_box['Total Leads'] = [total, allocate, pending]

        for lc in lc_obj:
           
            total = DataBank.objects.filter(lead_Id__lead_category_id__id=lc.id).count()
            allocate = DataBank.objects.filter(lead_Id__lead_category_id__id=lc.id,lead_allocate_status=1).count()
            pending = DataBank.objects.filter(lead_Id__lead_category_id__id=lc.id,lead_allocate_status=0).count()

            data_box[lc.lead_collection_for] = [total, allocate, pending]
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'leads_obj':leads_obj,
                   'notifications':notifications,
                   'lc_obj':lc_obj,
                   'data_box':data_box,
                   'employees':employees}
    return render(request,'DAM_clientPendingLeads.html',content)



def DAM_client_category_pendingLeads(request,lCID):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        employees = EmployeeRegister_Details.objects.filter(Q(emp_designation_id__dashboard_id=3) | Q(emp_designation_id__dashboard_id=5))

        lc = LeadCategory_Register.objects.get(id=lCID)

        cID = lc.cTaskId.client_Id.id

        lc_obj = LeadCategory_Register.objects.filter(cTaskId__client_Id=cID)

        leads_obj = DataBank.objects.filter(lead_Id__lead_category_id=lCID,lead_allocate_status=0)

        data_box = {}

        total = DataBank.objects.filter(lead_Id__lead_work_regId__clientId__id=cID).count()
        allocate = DataBank.objects.filter(lead_Id__lead_work_regId__clientId__id=cID,lead_allocate_status=1).count()
        pending = DataBank.objects.filter(lead_Id__lead_work_regId__clientId__id=cID,lead_allocate_status=0).count()

        data_box['Total Leads'] = [total, allocate, pending]

        for lc in lc_obj:
           
            total = DataBank.objects.filter(lead_Id__lead_category_id__id=lc.id).count()
            allocate = DataBank.objects.filter(lead_Id__lead_category_id__id=lc.id,lead_allocate_status=1).count()
            pending = DataBank.objects.filter(lead_Id__lead_category_id__id=lc.id,lead_allocate_status=0).count()

            data_box[lc.lead_collection_for] = [total, allocate, pending]

        viewdiv= True
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'leads_obj':leads_obj,
                   'notifications':notifications,
                   'lc_obj':lc_obj,
                   'viewdiv':viewdiv,
                   'data_box':data_box,
                   'employees':employees}
    return render(request,'DAM_clientPendingLeads.html',content)



def DMA_allocate_lead(request):

    if request.POST:

        leads_check = request.POST.getlist('lead_check')
        selected_emp = request.POST['selected_emp']
        for l in leads_check:
            db = DataBank.objects.get(id=l)
            db.lead_allocate_status = 1
            db.used_count += 1
            db.save()


        return redirect('DAM_client_pendingLeads',0)




# Data Manager Telecaller Dashboard 

def DAM_telecallers_dashboard(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}
    return render(request,'DAM_telecallerDashboard.html',content)




# Data Manager Platform Management

def DAM_platform_management(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        platform_data = PlatForms.objects.filter(company_Id=dash_details.emp_comp_id)
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'platform_data':platform_data}
        
    return render(request,'DAM_platform_management.html',content)


def DAM_platform_add(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        if request.POST:

            paltform_obj = PlatForms()
            paltform_obj.platform_Name = request.POST['platform_name']
            paltform_obj.company_Id = dash_details.emp_comp_id
            paltform_obj.save()

            platform_data = PlatForms.objects.filter(company_Id=dash_details.emp_comp_id)

            success = True
            success_text = 'New Platform add successfuly.'
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'success':success,
                   'success_text':success_text,
                   'platform_data':platform_data
                   }
        
    return render(request,'DAM_platform_management.html',content)

def DAM_platform_leads(request,pID):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        platform_data = PlatForms.objects.get(id=pID)
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'platform_data':platform_data
                   }
        
    return render(request,'DAM_platform_leads.html',content)



# Data Manager Waste Data Management 

def DAM_wasteData_management(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}
    return render(request,'DAM_watedata.html',content)



def DAM_logout(request):
    request.session['emp_id'] = ''
    return render(request,'login.html')