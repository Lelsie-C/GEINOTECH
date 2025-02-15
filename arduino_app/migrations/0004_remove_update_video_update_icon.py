# Generated by Django 5.1.5 on 2025-02-12 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arduino_app', '0003_remove_update_icon_update_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='update',
            name='video',
        ),
        migrations.AddField(
            model_name='update',
            name='icon',
            field=models.ImageField(blank=True, upload_to='icons/'),
        ),
    ]
