# Generated by Django 4.2.4 on 2023-08-29 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_shortlistedclubscouts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortlistedclubscouts',
            old_name='player',
            new_name='club',
        ),
    ]
