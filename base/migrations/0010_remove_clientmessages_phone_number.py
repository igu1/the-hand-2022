# Generated by Django 4.0.6 on 2022-07-28 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_clientmessages_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientmessages',
            name='phone_number',
        ),
    ]
