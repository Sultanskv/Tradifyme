# Generated by Django 5.0.6 on 2024-08-14 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_alter_ind_clientdt_clint_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ind_clientdt',
            name='clint_id',
            field=models.CharField(default='053a6bce', max_length=8, unique=True),
        ),
    ]
