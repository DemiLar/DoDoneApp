# Generated by Django 4.1 on 2022-08-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default='August 04, 2022'),
        ),
    ]