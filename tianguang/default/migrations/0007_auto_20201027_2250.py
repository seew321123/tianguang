# Generated by Django 2.0 on 2020-10-27 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0006_config'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
