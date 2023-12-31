# Generated by Django 3.2.8 on 2023-12-03 03:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='img',
            field=models.ImageField(upload_to='public/images/home/client', verbose_name='img'),
        ),
        migrations.AlterField(
            model_name='headerhome',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
