# Generated by Django 4.2.4 on 2023-09-10 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0030_newfeeds_likes_cout'),
    ]

    operations = [
        migrations.CreateModel(
            name='following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_followed', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]