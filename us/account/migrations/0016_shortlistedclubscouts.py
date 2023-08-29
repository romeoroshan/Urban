# Generated by Django 4.2.4 on 2023-08-29 03:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_shortlistedscouts'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortlistedClubScouts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shortlisted_club_scouts_as_player', to=settings.AUTH_USER_MODEL)),
                ('scout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shortlisted_club_scouts_as_scout', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]