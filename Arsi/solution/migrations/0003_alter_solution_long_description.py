# Generated by Django 3.2.8 on 2023-09-18 05:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0002_auto_20230918_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='long_description',
            field=ckeditor.fields.RichTextField(default='', null=True, verbose_name='Long Description'),
        ),
    ]
