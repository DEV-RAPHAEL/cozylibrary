# Generated by Django 4.0.4 on 2022-05-11 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cozylibrary", "0002_book_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="views",
            field=models.IntegerField(default=0),
        ),
    ]
