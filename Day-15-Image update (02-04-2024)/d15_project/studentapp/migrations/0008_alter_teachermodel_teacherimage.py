# Generated by Django 5.0.3 on 2024-04-01 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0007_alter_teachermodel_teacherimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='TeacherImage',
            field=models.ImageField(null=True, upload_to='media/Teacher_Image/'),
        ),
    ]