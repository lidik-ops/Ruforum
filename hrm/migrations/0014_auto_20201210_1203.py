# Generated by Django 2.2.2 on 2020-12-10 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0013_auto_20201210_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveassignment',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]