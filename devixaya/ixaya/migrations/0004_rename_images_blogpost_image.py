# Generated by Django 4.2.4 on 2023-08-24 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ixaya', '0003_rename_entryblog_blogpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='images',
            new_name='image',
        ),
    ]
