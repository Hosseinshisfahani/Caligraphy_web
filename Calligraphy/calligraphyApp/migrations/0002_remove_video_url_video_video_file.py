# Generated by Django 5.1.6 on 2025-02-24 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calligraphyApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.AddField(
            model_name='video',
            name='video_file',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]
