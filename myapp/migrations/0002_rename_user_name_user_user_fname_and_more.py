# Generated by Django 4.1.7 on 2023-04-22 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='User_Name',
            new_name='User_fName',
        ),
        migrations.RemoveField(
            model_name='user',
            name='User_Type',
        ),
        migrations.AddField(
            model_name='course',
            name='Course_Description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='User_City',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='User_Pos',
            field=models.CharField(choices=[('SA', 'Supervisor'), ('TA', 'Teaching Assistant'), ('IN', 'Instructor')], default='TA', max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='User_lName',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='Course_isOnline',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='section',
            name='Sec_isOnline',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='User_Address',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='User_Email',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='User_LogName',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='User_LogPass',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='User_Phone',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='User_isGrader',
            field=models.BooleanField(default=False),
        ),
    ]
