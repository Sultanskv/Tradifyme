# Generated by Django 5.0.4 on 2024-07-24 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_ind_clientdt_clint_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ind_clientdt',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ind_clientdt',
            name='login_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ind_clientdt',
            name='service_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ind_clientdt',
            name='strategies',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trade',
            name='lot_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trade',
            name='order_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ind_clientdt',
            name='auth_token',
            field=models.CharField(blank=True, max_length=1355, null=True),
        ),
        migrations.AlterField(
            model_name='ind_clientdt',
            name='clint_id',
            field=models.CharField(default='c1075ff3', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='ind_clientdt',
            name='feed_token',
            field=models.CharField(blank=True, max_length=1355, null=True),
        ),
        migrations.AlterField(
            model_name='ind_clientdt',
            name='refresh_token',
            field=models.CharField(blank=True, max_length=1355, null=True),
        ),
    ]
