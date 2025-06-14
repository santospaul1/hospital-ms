# Generated by Django 4.2.20 on 2025-04-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('address', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('enrolled_programs', models.ManyToManyField(blank=True, related_name='clients', to='programs.healthprogram')),
            ],
        ),
    ]
