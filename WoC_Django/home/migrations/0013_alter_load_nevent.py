# Generated by Django 4.0 on 2022-01-23 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_name_load_fname_load_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='nevent',
            field=models.CharField(max_length=122),
        ),
    ]
