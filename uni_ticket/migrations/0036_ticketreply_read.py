# Generated by Django 2.2.3 on 2019-07-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0035_auto_20190725_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketreply',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
