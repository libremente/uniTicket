# Generated by Django 2.2.1 on 2019-05-13 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0027_delete_taskattachment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TicketAttachment',
        ),
    ]
