# Generated by Django 2.2.1 on 2019-05-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0024_auto_20190507_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketcategorycondition',
            name='is_printable',
            field=models.BooleanField(default=False, verbose_name='Visibile nella versione stampabile'),
        ),
    ]
