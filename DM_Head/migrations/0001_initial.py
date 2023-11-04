# Generated by Django 4.1.2 on 2023-11-04 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Registration_Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allocation_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allocate_status', models.IntegerField(default=0)),
                ('alloaction_date', models.DateField(null=True)),
                ('allocatEmp_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.employeeregister_details')),
                ('allocat_to', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='EmployeeRegister', to='Registration_Login.employeeregister_details')),
            ],
        ),
        migrations.CreateModel(
            name='ClientRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client_email_primary', models.EmailField(blank=True, default='client@gmail.com', max_length=254, null=True)),
                ('client_email_alter', models.EmailField(blank=True, default='client@gmail2.com', max_length=254, null=True)),
                ('client_phone', models.CharField(blank=True, default='9000000009', max_length=255, null=True)),
                ('client_phone_alter', models.CharField(blank=True, default='9800000089', max_length=255, null=True)),
                ('client_address1', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client_address2', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client_address3', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client_place', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client_district', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client_state', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client_profile', models.ImageField(default='', upload_to='client\\profile')),
                ('client_bussiness_name', models.CharField(blank=True, default='9000000009', max_length=255, null=True)),
                ('client_bussiness_email_primary', models.EmailField(blank=True, default='client@gmail.com', max_length=254, null=True)),
                ('client_bussiness_email_alter', models.EmailField(blank=True, default='client@gmail2.com', max_length=254, null=True)),
                ('client_bussiness_phone', models.CharField(blank=True, default='9000000009', max_length=255, null=True)),
                ('client_bussiness_website', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client_bussiness_phone_alter', models.CharField(blank=True, default='9800000089', max_length=255, null=True)),
                ('client_bussiness_address1', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client_bussiness_address2', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client_bussiness_address3', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client_bussiness_place', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client_bussiness_district', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client_bussiness_state', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client_bussiness_file', models.ImageField(default='', upload_to='client\\files')),
                ('bussiness_logo', models.ImageField(default='', upload_to='client\\logo')),
                ('more_discription', models.TextField(blank=True, default='', null=True)),
                ('client_add_time', models.TimeField(auto_now_add=True, null=True)),
                ('client_status', models.IntegerField(default=0)),
                ('client_reg_date', models.DateField(auto_now=True, null=True)),
                ('compId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.businessregister_details')),
            ],
        ),
        migrations.CreateModel(
            name='ClientTask_Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('task_discription', models.TextField(blank=True, default='', null=True)),
                ('task_file', models.FileField(default='', upload_to='work\\task\\files')),
                ('task_allocate_status', models.IntegerField(default=0)),
                ('task_total_progress', models.IntegerField(default=0)),
                ('task_status', models.IntegerField(default=0)),
                ('task_create_date', models.DateField(null=True)),
                ('cTcompId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.businessregister_details')),
                ('client_Id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.clientregister')),
            ],
        ),
        migrations.CreateModel(
            name='TaskAssign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ta_discription', models.TextField(blank=True, default='', null=True)),
                ('ta_file', models.FileField(default='', upload_to='work\\files')),
                ('ta_progress', models.IntegerField(default=0)),
                ('ta_allocate_date', models.DateField(null=True)),
                ('ta_start_date', models.DateField(null=True)),
                ('ta_due_date', models.DateField(null=True)),
                ('ta_target', models.IntegerField(default=0)),
                ('ta_target_achived', models.IntegerField(default=0)),
                ('ta_status', models.IntegerField(default=0)),
                ('ta_accept_status', models.IntegerField(default=0)),
                ('ta_accept_date', models.DateField(null=True)),
                ('ta_type', models.IntegerField(default=0)),
                ('ta_taskId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.clienttask_register')),
            ],
        ),
        migrations.CreateModel(
            name='WorkAssign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wa_discription', models.TextField(blank=True, default='', null=True)),
                ('wa_file', models.FileField(default='', upload_to='work\\files')),
                ('work_assign_progress', models.IntegerField(default=0)),
                ('work_assign_date', models.DateField(auto_now=True, null=True)),
                ('wa_from_date', models.DateField(null=True)),
                ('wa_due_date', models.DateField(null=True)),
                ('wa_status', models.IntegerField(default=0)),
                ('wa_type', models.IntegerField(default=0)),
                ('allocated_exemp', models.ManyToManyField(related_name='co_works_allocated', to='Registration_Login.employeeregister_details')),
                ('wa_clientId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.clientregister')),
                ('wa_compId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.businessregister_details')),
                ('wa_tasksId', models.ManyToManyField(related_name='task_allocated', to='DM_Head.clienttask_register')),
                ('wa_work_allocate', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allocated_tl', to='Registration_Login.employeeregister_details')),
            ],
        ),
        migrations.CreateModel(
            name='WorkRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_discription', models.TextField(blank=True, default='', null=True)),
                ('work_create_time', models.TimeField(auto_now_add=True, null=True)),
                ('work_file', models.FileField(default='', upload_to='work\\files')),
                ('work_progress', models.IntegerField(default=0)),
                ('work_allocate_status', models.IntegerField(default=0)),
                ('work_status', models.IntegerField(default=0)),
                ('work_create_date', models.DateField(null=True)),
                ('work_end_date', models.DateField(null=True)),
                ('allocated_emp', models.ManyToManyField(related_name='works_allocated', to='Registration_Login.employeeregister_details')),
                ('clientId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.clientregister')),
                ('wcompId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.businessregister_details')),
            ],
        ),
        migrations.CreateModel(
            name='WorkProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp_add_date', models.DateField(auto_now=True, null=True)),
                ('work_discription', models.TextField(blank=True, default='', null=True)),
                ('wp_type', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('wp_progress', models.IntegerField(default=0)),
                ('wp_status', models.IntegerField(default=0)),
                ('wp_file', models.JSONField(default=list)),
                ('wp_workAssignId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.workassign')),
                ('wp_workerId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.employeeregister_details')),
            ],
        ),
        migrations.AddField(
            model_name='workassign',
            name='wa_work_regId',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.workregister'),
        ),
        migrations.CreateModel(
            name='Work_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('task_discription', models.TextField(blank=True, default='', null=True)),
                ('task_add_time', models.TimeField(auto_now_add=True, null=True)),
                ('task_status', models.IntegerField(default=0)),
                ('task_add_date', models.DateField(auto_now=True, null=True)),
                ('comp_taskid', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.businessregister_details')),
            ],
        ),
        migrations.CreateModel(
            name='TaskDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tad_collect_date', models.DateField(auto_now=True, null=True)),
                ('tad_title', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('tad_discription', models.TextField(blank=True, default='', null=True)),
                ('tad_file', models.JSONField(default=list)),
                ('tad_target', models.IntegerField(default=0)),
                ('tad_status', models.IntegerField(default=0)),
                ('tad_verified_target', models.IntegerField(default=0)),
                ('tad_taskAssignId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.taskassign')),
            ],
        ),
        migrations.AddField(
            model_name='taskassign',
            name='ta_workAssignId',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.workassign'),
        ),
        migrations.AddField(
            model_name='taskassign',
            name='ta_workerId',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.employeeregister_details'),
        ),
        migrations.CreateModel(
            name='Previos_Allocation_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_from_date', models.DateField(null=True)),
                ('previous_to_date', models.DateField(null=True)),
                ('previousemp_id', models.IntegerField(default=0)),
                ('previousemp_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('previousemp_allocatedTo', models.IntegerField(default=0)),
                ('previousemp_allocatedName', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('allocate_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.allocation_details')),
                ('newallocation_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.employeeregister_details')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notific_head', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('notific_content', models.TextField(blank=True, default='', null=True)),
                ('notific_time', models.TimeField(auto_now_add=True, null=True)),
                ('notific_status', models.IntegerField(default=0)),
                ('notific_date', models.DateField(auto_now=True, null=True)),
                ('emp_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.employeeregister_details')),
            ],
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('lead_email', models.EmailField(blank=True, default='', max_length=254, null=True)),
                ('lead_contact', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('lead_add_date', models.DateField(auto_now=True, null=True)),
                ('lead_add_time', models.TimeField(auto_now_add=True, null=True)),
                ('waste_data', models.IntegerField(default=0)),
                ('lead_status', models.IntegerField(default=0)),
                ('lead_transfer_date', models.DateField(null=True)),
                ('lead_transfer_status', models.IntegerField(default=0)),
                ('lead_collect_Emp_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.employeeregister_details')),
                ('lead_work_regId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.workregister')),
            ],
        ),
        migrations.CreateModel(
            name='LeadField_Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('field_discription', models.TextField(blank=True, default='', null=True)),
                ('field_add_time', models.TimeField(auto_now_add=True, null=True)),
                ('field_status', models.IntegerField(default=0)),
                ('field_add_date', models.DateField(auto_now=True, null=True)),
                ('field_clientId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.clientregister')),
                ('field_work_regId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.workregister')),
            ],
        ),
        migrations.CreateModel(
            name='lead_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_field_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('lead_field_data', models.CharField(blank=True, default='', max_length=855, null=True)),
                ('leadId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.leads')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_id', models.IntegerField(default=0)),
                ('from_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('feedback_content', models.TextField(blank=True, default='', null=True)),
                ('feedback_date', models.DateField(null=True)),
                ('feedback_emp_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.employeeregister_details')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(blank=True, default='', null=True)),
                ('end_time', models.TimeField(blank=True, default='', null=True)),
                ('schedule_head', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('todo_content', models.TextField(blank=True, default='', null=True)),
                ('log_time', models.TimeField(auto_now_add=True, null=True)),
                ('schedule_status', models.IntegerField(default=0)),
                ('schedule_date', models.DateField(null=True)),
                ('emp_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.employeeregister_details')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, default='', null=True)),
                ('end_date', models.DateField(blank=True, default='', null=True)),
                ('leave_type', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('leave_reason', models.TextField(blank=True, default='', null=True)),
                ('no_of_days', models.IntegerField(default=0)),
                ('leave_status', models.IntegerField(default=0)),
                ('leave_apply_date', models.DateField(null=True)),
                ('leave_statuChange_date', models.DateField(null=True)),
                ('leave_request_file', models.FileField(default='', upload_to='leave\\files')),
                ('emp_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.employeeregister_details')),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compaint_head', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('compaint_content', models.TextField(blank=True, default='', null=True)),
                ('complaint_date', models.DateField(auto_now=True, null=True)),
                ('action', models.TextField(blank=True, default='', null=True)),
                ('action_date', models.DateField(null=True)),
                ('status', models.IntegerField(default=0)),
                ('complaint_emp_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.employeeregister_details')),
            ],
        ),
        migrations.AddField(
            model_name='clienttask_register',
            name='work_Id',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.workregister'),
        ),
        migrations.CreateModel(
            name='ActionTaken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_from_id', models.IntegerField(default=0)),
                ('act_from_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('act_reason', models.TextField(blank=True, default='', null=True)),
                ('act_head', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('act_content', models.TextField(blank=True, default='', null=True)),
                ('action_date', models.DateField(null=True)),
                ('status', models.IntegerField(default=0)),
                ('act_emp_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.employeeregister_details')),
            ],
        ),
    ]
