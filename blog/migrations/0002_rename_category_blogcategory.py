# Generated by Django 4.2 on 2024-03-27 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='BlogCategory',
        ),
    ]
