# Generated by Django 5.0 on 2024-01-05 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_todo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='image',
            field=models.ImageField(default='https://m.media-amazon.com/images/I/31RvOPlfH7L.png', upload_to=''),
        ),
    ]
