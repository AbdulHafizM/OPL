# Generated by Django 4.1.1 on 2022-09-17 17:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_admission'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
