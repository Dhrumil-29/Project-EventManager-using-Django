# Generated by Django 4.0 on 2022-01-30 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_rename_sending_event_registration'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='load',
            new_name='Participant_Registration',
        ),
    ]
