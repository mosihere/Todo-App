# Generated by Django 5.0 on 2024-03-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0015_alter_todo_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]