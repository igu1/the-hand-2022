# Generated by Django 4.0.6 on 2022-07-30 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_clientmessages_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientmessages',
            name='phone_number',
            field=models.CharField(max_length=12, null=True),
        ),
    ]