# Generated by Django 4.1.7 on 2023-03-13 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_formApp', '0003_customdjangojob_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='jobstore',
        ),
        migrations.DeleteModel(
            name='CustomDjangoJob',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
