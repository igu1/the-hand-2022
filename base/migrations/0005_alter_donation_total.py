# Generated by Django 4.0.6 on 2022-07-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_donationautherization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
