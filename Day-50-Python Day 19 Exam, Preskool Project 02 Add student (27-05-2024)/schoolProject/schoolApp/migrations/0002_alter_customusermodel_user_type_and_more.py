# Generated by Django 5.0.6 on 2024-05-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='user_type',
            field=models.CharField(choices=[('3', 'student'), ('1', 'admin'), ('2', 'teacher')], max_length=100),
        ),
        migrations.AlterField(
            model_name='studentaddmodel',
            name='Gender',
            field=models.CharField(choices=[('male', 'Male'), ('others', 'Others'), ('female', 'Female')], max_length=100),
        ),
        migrations.AlterField(
            model_name='studentaddmodel',
            name='Section',
            field=models.CharField(choices=[('2', 'B'), ('3', 'C'), ('4', 'D'), ('1', 'A')], max_length=100),
        ),
        migrations.AlterField(
            model_name='studentaddmodel',
            name='Session_Year',
            field=models.CharField(choices=[('1', 'Summer Session'), ('2', 'Fall Session'), ('3', 'Spring Session')], max_length=100),
        ),
    ]