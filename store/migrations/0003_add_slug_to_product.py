# Generated by Django 3.2.6 on 2021-08-08 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_price_to_unit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='-'),
            preserve_default=False,
        ),
    ]
