# Generated by Django 2.2.4 on 2019-08-06 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unical_accounts', '0006_remove_user_is_operator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_utente',
        ),
    ]
