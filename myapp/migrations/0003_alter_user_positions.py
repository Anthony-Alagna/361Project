# Generated by Django 4.2 on 2023-05-18 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_course_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='positions',
            field=models.CharField(blank=True, choices=[('SA', 'Supervisor'), ('TA', 'Teaching Assistant'), ('IN', 'Instructor')], default='SA', max_length=2),
        ),
    ]
