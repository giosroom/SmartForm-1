# Generated by Django 4.1.7 on 2023-03-14 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_emailApp', '0008_rename_scheduledjob_customscheduledjob'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomScheduledJob',
            new_name='Custom_ScheduledJob',
        ),
    ]
