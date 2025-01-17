# Generated by Django 4.2.4 on 2024-03-06 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0059_scoutplayers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoutPlayerResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('scout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.scoutplayers')),
            ],
        ),
    ]
