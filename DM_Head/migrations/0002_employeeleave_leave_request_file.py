# Generated by Django 4.1.2 on 2023-10-31 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DM_Head', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeleave',
            name='leave_request_file',
            field=models.FileField(default='', upload_to='leave\\files'),
        ),
    ]
