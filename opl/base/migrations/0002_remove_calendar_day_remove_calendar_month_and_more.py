# Generated by Django 4.1.1 on 2022-09-12 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='day',
        ),
        migrations.RemoveField(
            model_name='calendar',
            name='month',
        ),
        migrations.RemoveField(
            model_name='calendar',
            name='year',
        ),
        migrations.AlterField(
            model_name='calendar',
            name='date',
            field=models.CharField(max_length=25),
        ),
    ]