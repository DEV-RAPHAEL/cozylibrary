# Generated by Django 4.0.4 on 2022-05-10 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cozylibrary", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="created_at",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
