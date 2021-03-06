# Generated by Django 2.2.4 on 2019-08-07 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0044_auto_20190807_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcategory',
            name='allow_employee',
            field=models.BooleanField(default=True, verbose_name="Accessibile ai dipendenti dell'organizzazione"),
        ),
        migrations.AlterField(
            model_name='ticketcategory',
            name='allow_guest',
            field=models.BooleanField(default=True, verbose_name='Accessibile agli ospiti'),
        ),
        migrations.AlterField(
            model_name='ticketcategory',
            name='allow_user',
            field=models.BooleanField(default=True, verbose_name="Accessibile agli utenti dell'organizzazione"),
        ),
    ]
