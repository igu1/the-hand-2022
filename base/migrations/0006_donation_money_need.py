# Generated by Django 4.0.6 on 2022-07-27 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_donation_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='money_need',
            field=models.FloatField(default=0),
        ),
    ]
