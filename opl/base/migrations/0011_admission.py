# Generated by Django 4.1.1 on 2022-09-15 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_blog_body_blog_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=2)),
                ('student_class', models.CharField(choices=[('jss1', 'JSS1'), ('jss2', 'JSS2'), ('jss3', 'JSS3'), ('ss1', 'SS1'), ('ss2', 'SS2'), ('ss3', 'SS3')], default='jss1', max_length=4)),
                ('parent_name', models.CharField(max_length=25)),
                ('number', models.CharField(max_length=11)),
                ('address', models.TextField()),
            ],
        ),
    ]