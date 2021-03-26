# Generated by Django 3.1.7 on 2021-03-19 02:24

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='Meerkat', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, max_length=255, upload_to=users.models.nameFile),
        ),
    ]
