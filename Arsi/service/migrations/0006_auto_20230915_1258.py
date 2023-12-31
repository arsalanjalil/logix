# Generated by Django 3.2.8 on 2023-09-15 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('industry', '0002_alter_industry_short_description'),
        ('service', '0005_auto_20230915_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='industry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='industry.industry'),
        ),
        migrations.AlterField(
            model_name='service',
            name='parent',
            field=models.ForeignKey(db_constraint=False, default=0, on_delete=django.db.models.deletion.CASCADE, to='service.service'),
        ),
    ]
