# Generated by Django 4.0.6 on 2022-08-27 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InterSteller', '0034_signup_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignupChecking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Names', models.CharField(max_length=50)),
                ('Emails', models.CharField(max_length=50)),
                ('Passwords', models.CharField(max_length=50)),
                ('Moneys', models.IntegerField()),
                ('verification', models.CharField(max_length=50)),
                ('idx', models.CharField(max_length=500)),
                ('refer', models.CharField(max_length=50)),
                ('refer_by', models.CharField(max_length=50)),
                ('UserId', models.CharField(max_length=50)),
            ],
        ),
    ]
