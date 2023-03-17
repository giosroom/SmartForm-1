# Generated by Django 4.1.7 on 2023-03-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_formApp', '0002_user_welcome_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='welcome_email',
        ),
        migrations.AddField(
            model_name='user',
            name='email_agreements',
            field=models.BooleanField(default=True),
        ),
    ]
