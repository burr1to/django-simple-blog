# Generated by Django 3.2.9 on 2021-12-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211212_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_content',
            field=models.TextField(default=' '),
        ),
    ]
