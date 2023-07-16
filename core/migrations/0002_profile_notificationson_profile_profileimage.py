# Generated by Django 4.1.7 on 2023-06-24 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='notificationson',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profileimage',
            field=models.ImageField(default='blank-profile-picture.png', upload_to='profileimgs'),
        ),
    ]
