# Generated by Django 2.2.2 on 2020-12-09 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants_reports', '0002_auto_20201208_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firststudentreport',
            name='tuition_paid',
            field=models.IntegerField(choices=[(None, '--please select--'), (2, 'Yes'), (3, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='studentmonth12report',
            name='research_objectives',
            field=models.TextField(blank=True, null=True),
        ),
    ]
