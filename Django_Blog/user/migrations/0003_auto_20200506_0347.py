# Generated by Django 3.0.4 on 2020-05-06 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='text',
            field=models.CharField(max_length=50),
        ),
    ]
