# Generated by Django 2.1.5 on 2019-02-25 10:31

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_website_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='dnt',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]
