# Generated by Django 4.0.6 on 2022-08-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InterSteller', '0011_rename_email_signup_emails_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_cheking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Names', models.CharField(max_length=50)),
                ('Emails', models.CharField(max_length=50)),
                ('Passwords', models.CharField(max_length=50)),
                ('Moneys', models.IntegerField()),
                ('otp_verify', models.CharField(max_length=50)),
            ],
        ),
    ]
