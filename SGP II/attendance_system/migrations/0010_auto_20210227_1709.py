# Generated by Django 3.0.8 on 2021-02-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_system', '0009_auto_20210227_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='fname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='lname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]