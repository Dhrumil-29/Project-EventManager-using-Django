# Generated by Django 4.0 on 2022-01-20 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_send_load'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='nopar',
            field=models.IntegerField(default=1),
        ),
    ]