# Generated by Django 3.1.1 on 2020-09-17 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_auto_20200917_0932'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GameEdition',
        ),
    ]
