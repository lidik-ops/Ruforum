# Generated by Django 2.2.2 on 2020-12-10 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0012_auto_20201208_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaveassignment',
            name='staff',
        ),
        migrations.AddField(
            model_name='leaveassignment',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leave_assignments', to='hrm.StaffProfile'),
        ),
    ]