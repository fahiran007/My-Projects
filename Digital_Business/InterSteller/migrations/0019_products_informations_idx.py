# Generated by Django 4.0.6 on 2022-08-20 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InterSteller', '0018_remove_products_sr_products_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='products_informations',
            name='idx',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
