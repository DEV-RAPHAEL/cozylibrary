# Generated by Django 4.0.4 on 2022-05-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cozylibrary', '0005_alter_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='Dapo Adedire', max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(default='English', max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='Dapo Adedire', max_length=255),
        ),
    ]
