# Generated by Django 5.1.6 on 2025-03-11 12:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooler', '0002_taskers_alter_task_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='tasker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cooler.taskers'),
        ),
    ]
