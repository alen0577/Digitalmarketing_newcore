# Generated by Django 4.1.2 on 2023-11-13 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DM_Head', '0003_remove_workprogress_wp_workassignid'),
    ]

    operations = [
        migrations.AddField(
            model_name='workassign',
            name='wa_target',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='workassign',
            name='wa_target_achived',
            field=models.IntegerField(default=0),
        ),
    ]