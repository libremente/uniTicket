# Generated by Django 2.1.7 on 2019-04-04 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_ticket', '0002_remove_ticketreply_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketreply',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
