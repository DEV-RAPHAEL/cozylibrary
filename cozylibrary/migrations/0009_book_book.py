# Generated by Django 4.0.4 on 2022-05-13 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cozylibrary', '0008_remove_book_download_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book',
            field=models.FileField(default='/books/default.pdf', upload_to='books/'),
        ),
    ]
