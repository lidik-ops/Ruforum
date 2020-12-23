# Generated by Django 2.2.2 on 2020-12-03 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grants', '0001_initial'),
        ('PI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectevent',
            name='grant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grant', to='grants.Grant'),
        ),
        migrations.AddField(
            model_name='projectevent',
            name='organiser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='pi', to=settings.AUTH_USER_MODEL),
        ),
    ]