# Generated by Django 2.0 on 2017-12-28 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='images',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
