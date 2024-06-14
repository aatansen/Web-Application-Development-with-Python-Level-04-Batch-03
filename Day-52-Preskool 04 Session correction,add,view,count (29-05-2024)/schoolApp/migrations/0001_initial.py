# Generated by Django 5.0.6 on 2024-05-28 12:20

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentAddModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department_Name', models.CharField(max_length=100)),
                ('Head_of_Department', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SessionAddModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Session_Year', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('2', 'teacher'), ('1', 'admin'), ('3', 'student')], max_length=100)),
                ('user_img', models.ImageField(upload_to='static/user_img')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
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
            name='StudentAddModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Id', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=100)),
                ('Section', models.CharField(choices=[('4', 'D'), ('2', 'B'), ('3', 'C'), ('1', 'A')], max_length=100)),
                ('Date_of_Birth', models.DateField()),
                ('Religion', models.CharField(max_length=100)),
                ('Mobile_Number', models.CharField(max_length=100)),
                ('Student_Image', models.ImageField(upload_to='static/Student_Image')),
                ('Father_Name', models.CharField(max_length=100)),
                ('Father_Occupation', models.CharField(max_length=100)),
                ('Father_Mobile', models.CharField(max_length=100)),
                ('Father_Email', models.EmailField(max_length=100)),
                ('Mother_Name', models.CharField(max_length=100)),
                ('Mother_Occupation', models.CharField(max_length=100)),
                ('Mother_Mobile', models.CharField(max_length=100)),
                ('Mother_Email', models.EmailField(max_length=100)),
                ('Present_Address', models.TextField()),
                ('Permanent_Address', models.TextField()),
                ('myDepartment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='schoolApp.departmentaddmodel')),
                ('mySessionYear', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='schoolApp.sessionaddmodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
