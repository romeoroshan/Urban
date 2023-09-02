# Generated by Django 4.2.4 on 2023-08-31 06:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_postimagefeed'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostVideoFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to='pics', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_video_feed_as_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]