# Generated by Django 3.1.6 on 2021-05-02 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_system', '0023_auto_20210410_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='total_hour',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]