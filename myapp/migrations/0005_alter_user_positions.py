# Generated by Django 4.2 on 2023-05-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_user_positions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='positions',
            field=models.CharField(blank=True, default='Supervisor', max_length=25),
        ),
    ]