# Generated by Django 4.1.7 on 2023-03-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_emailApp', '0005_alter_emailtask_priority_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtask',
            name='job_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
