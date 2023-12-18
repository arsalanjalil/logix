# Generated by Django 3.2.8 on 2023-12-18 03:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0004_solution_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='code',
            field=ckeditor.fields.RichTextField(default=' '),
        ),
        migrations.AddField(
            model_name='feature',
            name='img',
            field=models.ImageField(null=True, upload_to='public/images/solution/solutions/features', verbose_name='banner'),
        ),
    ]
