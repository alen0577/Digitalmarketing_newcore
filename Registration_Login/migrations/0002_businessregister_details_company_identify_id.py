# Generated by Django 4.1.2 on 2023-12-01 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration_Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessregister_details',
            name='company_identify_Id',
            field=models.CharField(default='COMID001', max_length=150),
        ),
    ]