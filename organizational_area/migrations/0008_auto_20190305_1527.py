# Generated by Django 2.1.7 on 2019-03-05 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizational_area', '0007_auto_20190305_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationalstructureadmin',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='organizationalstructureadmin',
            name='structure',
        ),
        migrations.DeleteModel(
            name='OrganizationalStructureAdmin',
        ),
    ]
