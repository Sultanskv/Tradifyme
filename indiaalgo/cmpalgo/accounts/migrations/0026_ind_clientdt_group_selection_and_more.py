# Generated by Django 5.0.6 on 2024-08-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_remove_ind_clientdt_client_option_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ind_clientdt',
            name='group_selection',
            field=models.CharField(choices=[('Alpha Wave', 'Alpha Wave'), ('Gamma Gains', 'Gamma Gains'), ('BetaBalance', 'BetaBalance'), ('Demograph', 'Demograph')], default='Alpha Wave', max_length=50),
        ),
        migrations.AlterField(
            model_name='ind_clientdt',
            name='clint_id',
            field=models.CharField(default='33374d1f', max_length=8, unique=True),
        ),
    ]
