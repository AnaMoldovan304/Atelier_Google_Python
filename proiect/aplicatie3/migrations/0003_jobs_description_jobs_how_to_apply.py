# Generated by Django 4.0.4 on 2022-05-10 09:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie3', '0002_jobs_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobs',
            name='how_to_apply',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
