# Generated by Django 4.0.6 on 2022-08-23 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InterSteller', '0031_delete_userlogin'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='UserId',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]