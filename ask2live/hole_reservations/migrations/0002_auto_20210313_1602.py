# Generated by Django 3.1.7 on 2021-03-13 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('holes', '0001_initial'),
        ('hole_reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='guests',
            field=models.ManyToManyField(blank=True, related_name='hole_reservations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reservation',
            name='hole',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='hole_reservations', to='holes.hole'),
        ),
    ]
