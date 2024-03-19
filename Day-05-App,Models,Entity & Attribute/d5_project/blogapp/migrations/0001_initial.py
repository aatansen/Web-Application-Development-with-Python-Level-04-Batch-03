# Generated by Django 5.0.3 on 2024-03-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('author_bio', models.CharField(max_length=100)),
                ('author_email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_date', models.CharField(max_length=100)),
                ('blog_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=100)),
                ('comment_date', models.CharField(max_length=100)),
                ('commenter_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_headings', models.CharField(max_length=100)),
                ('news_date', models.CharField(max_length=100)),
                ('news_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
                ('tag_description', models.CharField(max_length=100)),
                ('tag_items', models.CharField(max_length=100)),
            ],
        ),
    ]
