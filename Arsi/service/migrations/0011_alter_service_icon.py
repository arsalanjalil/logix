# Generated by Django 3.2.8 on 2023-12-03 22:51

from django.db import migrations
import faicon.fields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_auto_20231203_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=faicon.fields.FAIconField(max_length=50, null=True),
        ),
    ]
