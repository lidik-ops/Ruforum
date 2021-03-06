# Generated by Django 2.2.2 on 2020-12-03 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hrm', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=191)),
                ('from_date', models.DateTimeField(null=True)),
                ('to_date', models.DateTimeField(null=True)),
                ('budget', models.FloatField(blank=True, null=True)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('quarter_one_start_date', models.DateField()),
                ('quarter_one_end_date', models.DateField()),
                ('quarter_two_start_date', models.DateField()),
                ('quarter_two_end_date', models.DateField()),
                ('quarter_three_start_date', models.DateField()),
                ('quarter_three_end_date', models.DateField()),
                ('quarter_four_start_date', models.DateField()),
                ('quarter_four_end_date', models.DateField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particular', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FrameWorkUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator', models.CharField(max_length=191)),
                ('target_output', models.CharField(max_length=191)),
                ('unit_of_measure', models.FloatField()),
                ('means_of_verification', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pme.Activity')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resultarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_area', models.CharField(max_length=191)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=191)),
                ('task_description', models.TextField()),
                ('expectedoutput', models.PositiveIntegerField()),
                ('priority', models.IntegerField(choices=[(3, 'High'), (2, 'Medium'), (1, 'Low')])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pme.Activity')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='leading_tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=191)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hrm.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Workplan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplan_name', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pme.Resultarea')),
                ('financial_year', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pme.FinancialYear')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pme.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='TaskUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pme.Task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Taskreporting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_title', models.CharField(max_length=191)),
                ('reporting_date', models.DateField()),
                ('quarter', models.CharField(max_length=191)),
                ('output_target', models.CharField(max_length=191)),
                ('status', models.IntegerField()),
                ('percentage_progress', models.CharField(max_length=191)),
                ('target_met', models.IntegerField()),
                ('target_numbers', models.CharField(max_length=191)),
                ('description_of_achievement', models.CharField(max_length=191)),
                ('attachment', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pme.Indicator')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pme.Task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reports', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('not_started', 'Not started'), ('in_progress', 'In progress'), ('completed', 'Completed'), ('failed', 'Failed')], max_length=50)),
                ('has_file', models.BooleanField()),
                ('task_file', models.FileField(blank=True, null=True, upload_to='')),
                ('reported_on', models.DateField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='pme.Task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pme.Unit'),
        ),
        migrations.CreateModel(
            name='Sourceoffunding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_name', models.CharField(max_length=191)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milestone', models.CharField(max_length=191)),
                ('milestone_date', models.DateField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pme.Task')),
            ],
        ),
        migrations.CreateModel(
            name='Indicatorcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=191)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FrameworkResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField()),
                ('key_performance_indicator', models.CharField(max_length=300)),
                ('is_core', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('year', models.CharField(max_length=4)),
                ('baseline', models.CharField(max_length=300)),
                ('target', models.CharField(max_length=200)),
                ('actual', models.CharField(blank=True, max_length=200, null=True)),
                ('data_source', models.CharField(max_length=200)),
                ('collection_method', models.CharField(max_length=200)),
                ('rating_scale_methodology', models.TextField()),
                ('responsible_staff', models.CharField(max_length=100)),
                ('collection_frequency', models.CharField(max_length=50)),
                ('framework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pme.Framework')),
                ('unit_of_measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pme.FrameWorkUnit')),
            ],
        ),
        migrations.CreateModel(
            name='Expectedoutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output', models.FloatField()),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pme.Activity')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output', models.FloatField()),
                ('description', models.TextField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pme.Activity')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='sourceoffunding',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pme.Sourceoffunding'),
        ),
        migrations.AddField(
            model_name='activity',
            name='workplan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pme.Workplan'),
        ),
    ]
