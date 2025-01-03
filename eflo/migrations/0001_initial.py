# Generated by Django 4.2.6 on 2023-11-05 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job_listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_logo', models.ImageField(upload_to='')),
                ('job_title', models.CharField(max_length=300)),
                ('job_start', models.DateField(verbose_name='Start Date')),
                ('job_end', models.DateField(verbose_name='End Date')),
                ('job_description', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='log_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
                ('log_date', models.DateTimeField(verbose_name='date logged')),
            ],
        ),
    ]
