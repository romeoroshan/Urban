# Generated by Django 4.2.4 on 2023-09-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0029_rename_feed_id_likes_feed'),
    ]

    operations = [
        migrations.AddField(
            model_name='newfeeds',
            name='likes_cout',
            field=models.IntegerField(default=0),
        ),
    ]
