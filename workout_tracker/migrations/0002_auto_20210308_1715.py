# Generated by Django 3.1.7 on 2021-03-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workouttracker',
            name='workout',
            field=models.JSONField(default=dict),
        ),
    ]
