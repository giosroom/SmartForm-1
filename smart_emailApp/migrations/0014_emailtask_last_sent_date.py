# Generated by Django 4.1.7 on 2023-04-30 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("smart_emailApp", "0013_link_created_at_link_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="emailtask",
            name="last_sent_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
