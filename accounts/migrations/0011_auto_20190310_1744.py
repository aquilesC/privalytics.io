# Generated by Django 2.1.7 on 2019-03-10 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20190308_0856'),
        ('subscriptions', '0001_initial')
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='subscription_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.SubscriptionType'),
        ),
    ]