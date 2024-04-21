# Generated by Django 5.0.3 on 2024-03-19 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ai_name', models.CharField(max_length=100)),
                ('ai_usage', models.CharField(max_length=100)),
                ('ai_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DatasetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset_name', models.CharField(max_length=100)),
                ('dataset_format', models.CharField(max_length=100)),
                ('dataset_size', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExperimentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiment_name', models.CharField(max_length=100)),
                ('experiment_date', models.CharField(max_length=100)),
                ('experiment_results', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('task_deadline', models.CharField(max_length=100)),
                ('task_priority', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.CharField(max_length=100)),
                ('user_role', models.CharField(max_length=100)),
            ],
        ),
    ]