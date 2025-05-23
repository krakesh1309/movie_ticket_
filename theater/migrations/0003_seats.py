# Generated by Django 5.2 on 2025-04-14 10:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0002_showtimes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_number', models.IntegerField(blank=True, null=True)),
                ('row_label', models.CharField(max_length=10)),
                ('seat_number', models.IntegerField()),
                ('seat_type', models.CharField(choices=[('gold', 'Gold'), ('silver', 'Silver')], max_length=20)),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.theaters')),
            ],
        ),
    ]
