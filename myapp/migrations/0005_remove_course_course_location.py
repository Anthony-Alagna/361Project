# Generated by Django 4.2 on 2023-05-10 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_course_course_isonline_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='Course_Location',
        ),
    ]