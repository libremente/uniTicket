# Generated by Django 3.0 on 2020-01-07 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0052_ticketassignment_modified'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TicketHistory',
        ),
    ]
