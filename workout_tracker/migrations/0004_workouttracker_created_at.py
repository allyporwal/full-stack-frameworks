# Generated by Django 3.1.7 on 2021-03-15 10:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker', '0003_auto_20210308_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='workouttracker',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]