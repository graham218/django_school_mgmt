# Generated by Django 3.1.12 on 2021-10-28 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_auto_20211028_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=193632, unique=True),
        ),
    ]
