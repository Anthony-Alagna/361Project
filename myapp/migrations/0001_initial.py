# Generated by Django 4.2 on 2023-05-18 02:13

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('username', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(blank=True, max_length=200)),
                ('positions', models.CharField(blank=True, choices=[('SA', 'Supervisor'), ('TA', 'Teaching Assistant'), ('IN', 'Instructor')], max_length=25)),
                ('phone_number', models.CharField(blank=True, max_length=200)),
                ('address', models.TextField(blank=True, max_length=500)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('is_grader', models.BooleanField(default=False)),
                ('pw_reset_token', models.CharField(blank=True, default='', max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('isLoggedIn', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='course_id')),
                ('Course_Code', models.CharField(max_length=3)),
                ('Course_Name', models.CharField(max_length=50)),
                ('Course_Description', models.CharField(blank=True, max_length=150)),
                ('Course_Instructor', models.CharField(blank=True, max_length=50)),
                ('Course_Instruction_Method', models.CharField(blank=True, max_length=20)),
                ('Course_begin', models.DateTimeField(auto_now_add=True, null=True)),
                ('Course_Updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sec_Name', models.CharField(max_length=200)),
                ('Sec_Location', models.CharField(max_length=200)),
                ('Sec_isOnline', models.BooleanField(default=False)),
                ('Sec_begin', models.DateTimeField(auto_now_add=True, null=True)),
                ('Sec_Updated', models.DateTimeField(auto_now=True, null=True)),
                ('Sec_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
                ('Sec_Instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseEnrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_instructor', models.BooleanField(default=False)),
                ('is_TA', models.BooleanField(default=False)),
                ('is_grader', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Course Enrollments',
                'unique_together': {('course', 'user')},
            },
        ),
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(related_name='enrolled_courses', through='myapp.CourseEnrollment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='assigned_users', through='myapp.CourseEnrollment', to='myapp.course'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='sections',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_users', to='myapp.section'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
