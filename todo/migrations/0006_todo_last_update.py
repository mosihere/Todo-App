# Generated by Django 5.0 on 2024-01-01 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_todo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
