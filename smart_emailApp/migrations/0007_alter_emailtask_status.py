# Generated by Django 4.1.7 on 2023-03-15 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_emailApp', '0006_myjobmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtask',
            name='status',
            field=models.CharField(blank=True, choices=[('Scheduled', 'Scheduled'), ('Running', 'Running'), ('Not Scheduled', 'Not Scheduled'), ('Expired', 'Expired')], max_length=50, null=True),
        ),
    ]
