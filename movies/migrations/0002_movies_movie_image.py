# Generated by Django 5.1.2 on 2025-04-17 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='movie_image',
            field=models.ImageField(blank=True, null=True, upload_to='movie_image/'),
        ),
    ]
