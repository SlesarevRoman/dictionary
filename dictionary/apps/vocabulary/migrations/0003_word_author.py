# Generated by Django 3.1.4 on 2020-12-04 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vocabulary', '0002_auto_20201204_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='author',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
