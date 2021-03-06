# Generated by Django 2.2.2 on 2020-12-10 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fellowship_applications', '0003_auto_20201210_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fellowshipapplication',
            name='state',
        ),
        migrations.AddField(
            model_name='fellowshipapplication',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('validated', 'Validated'), ('noncompliant', 'Non Compliant'), ('rejected', 'Rejected'), ('selected_for_funding', 'Selected for Funding')], default='Submitted', max_length=20),
        ),
    ]
