# Generated by Django 3.2.9 on 2021-12-12 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_slug',
            field=models.SlugField(max_length=250, unique_for_date='blog_date'),
        ),
    ]
