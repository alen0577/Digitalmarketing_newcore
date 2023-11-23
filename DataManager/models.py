from django.db import models
from DM_Head.models import Leads
from Registration_Login.models import BusinessRegister_Details


class DataBank(models.Model):
    lead_Id = models.ForeignKey(Leads, on_delete=models.CASCADE, null=True,default='')
    Genarated_date = models.DateField(auto_now_add=True,null=True)
    used_count = models.IntegerField(default=0)
    lead_allocate_status = models.IntegerField(default=0)
    allocated_date = models.DateField(auto_now_add=False,null=True)

class PlatForms(models.Model):
    company_Id = models.ForeignKey(BusinessRegister_Details, on_delete=models.CASCADE, null=True,default='')
    created_date = models.DateField(auto_now_add=True,null=True)
    platform_Name = models.CharField(max_length=150,default='')
    platform_TotalCount = models.IntegerField(default=0)

class PlatFormsData(models.Model):
    data_add_date = models.DateField(auto_now_add=True,null=True)
    platform_name = models.CharField(max_length=150,default='')
    platform_dataCount = models.IntegerField(default=0)

