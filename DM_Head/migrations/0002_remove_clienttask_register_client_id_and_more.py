# Generated by Django 4.1.2 on 2023-10-26 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DM_Head', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clienttask_register',
            name='client_Id',
        ),
        migrations.RemoveField(
            model_name='clienttask_register',
            name='work_Id',
        ),
        migrations.RemoveField(
            model_name='work_task',
            name='comp_taskid',
        ),
        migrations.RemoveField(
            model_name='workregister',
            name='clientId',
        ),
        migrations.DeleteModel(
            name='ClientRegister',
        ),
        migrations.DeleteModel(
            name='ClientTask_Register',
        ),
        migrations.DeleteModel(
            name='Work_Task',
        ),
        migrations.DeleteModel(
            name='WorkRegister',
        ),
    ]
