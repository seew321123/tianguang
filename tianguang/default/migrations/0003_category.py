# Generated by Django 2.0 on 2020-09-13 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0002_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=1000)),
            ],
        ),
    ]