# Generated by Django 3.2.8 on 2023-09-18 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_auto_20230915_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='feature',
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True, verbose_name='name')),
                ('title', models.TextField()),
                ('svg', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.product', verbose_name='service_id')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True, verbose_name='name')),
                ('title', models.TextField()),
                ('img', models.ImageField(null=True, upload_to='public/images/services/service', verbose_name='img')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.product', verbose_name='service_id')),
            ],
        ),
        migrations.CreateModel(
            name='Detaile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=250, null=True, verbose_name='name')),
                ('svg', models.TextField()),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.feature', verbose_name='service_id')),
            ],
        ),
    ]
