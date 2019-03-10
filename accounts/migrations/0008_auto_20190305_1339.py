# Generated by Django 2.1.7 on 2019-03-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_account_selected'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='maximum_views',
            field=models.IntegerField(default=0, help_text='maximum number of views across all websites'),
        ),
        migrations.AddField(
            model_name='profile',
            name='monthly_views',
            field=models.IntegerField(default=0, help_text='number of views registered in the last month'),
        ),
    ]
