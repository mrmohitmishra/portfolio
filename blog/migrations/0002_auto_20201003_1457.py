# Generated by Django 2.2 on 2020-10-03 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_image',
            new_name='image',
        ),
    ]
