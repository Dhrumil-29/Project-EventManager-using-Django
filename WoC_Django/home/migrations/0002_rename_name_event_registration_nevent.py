# Generated by Django 4.0 on 2022-01-19 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event_registration',
            old_name='name',
            new_name='nEvent',
        ),
    ]
