# Generated by Django 5.0 on 2024-03-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_alter_todo_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
