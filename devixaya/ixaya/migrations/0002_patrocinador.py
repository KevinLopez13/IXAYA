# Generated by Django 4.2.4 on 2023-08-24 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ixaya', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patrocinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
    ]
