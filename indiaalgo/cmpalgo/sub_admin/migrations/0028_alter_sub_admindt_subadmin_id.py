# Generated by Django 5.0.6 on 2024-08-13 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_admin', '0027_alter_sub_admindt_subadmin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_admindt',
            name='subadmin_id',
            field=models.CharField(default='b2aaf573', max_length=8, unique=True),
        ),
    ]
