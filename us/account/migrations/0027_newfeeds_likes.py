# Generated by Django 4.2.4 on 2023-09-05 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_newfeeds_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='newfeeds',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]