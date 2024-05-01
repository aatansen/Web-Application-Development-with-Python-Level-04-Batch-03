# Generated by Django 5.0.4 on 2024-04-29 06:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeApp', '0002_recipemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='ingredients',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='ChefProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(max_length=100)),
                ('skill', models.CharField(max_length=100)),
                ('resume_latter', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(upload_to='static/profile_pic')),
                ('myuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ViewerProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favourite', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(upload_to='static/profile_pic')),
                ('myuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]