# Generated by Django 2.1.7 on 2019-03-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20190305_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttypes',
            name='monthly_price',
            field=models.IntegerField(default=0, help_text='Monthly price in dollars'),
        ),
        migrations.AlterField(
            model_name='accounttypes',
            name='yearly_price',
            field=models.IntegerField(default=0, help_text='Yearly price in dollars'),
        ),
    ]
