# Generated by Django 4.0.4 on 2022-05-10 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('category', models.CharField(blank=True, max_length=255)),
                ('pages', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.99)),
                ('year', models.IntegerField(default=0)),
                ('language', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('cover_image', models.ImageField(blank=True, default='/covers/default.jpg', upload_to='covers/')),
            ],
        ),
    ]
