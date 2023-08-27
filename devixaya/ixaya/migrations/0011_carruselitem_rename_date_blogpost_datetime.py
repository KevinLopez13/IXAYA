# Generated by Django 4.2.4 on 2023-08-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ixaya', '0010_patrocinador_image_alter_blogpost_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarruselItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carrusel/')),
            ],
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='date',
            new_name='datetime',
        ),
    ]
