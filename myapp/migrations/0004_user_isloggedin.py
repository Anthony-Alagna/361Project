# Generated by Django 4.2 on 2023-05-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_user_pw_reset_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isLoggedIn',
            field=models.BooleanField(default=False),
        ),
    ]