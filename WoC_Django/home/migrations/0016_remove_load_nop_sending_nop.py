# Generated by Django 4.0 on 2022-01-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_load_nop_alter_load_nopar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='load',
            name='nop',
        ),
        migrations.AddField(
            model_name='sending',
            name='nop',
            field=models.IntegerField(default='0'),
        ),
    ]
