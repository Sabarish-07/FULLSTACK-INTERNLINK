# Generated by Django 5.1.2 on 2024-10-27 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.BinaryField(null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('intern_id', models.CharField(max_length=50)),
                ('team', models.CharField(choices=[('Rewards Team', 'Rewards Team'), ('Skill Team', 'Skill Team'), ('Academics', 'Academics'), ('T&P', 'T&P'), ('R&D', 'R&D'), ('PIC', 'PIC')], max_length=50)),
                ('mobile_number', models.CharField(max_length=15)),
                ('alt_mobile_number', models.CharField(blank=True, max_length=15)),
                ('personal_email', models.EmailField(max_length=100)),
                ('institution_email', models.EmailField(max_length=100)),
                ('reporting_head', models.CharField(max_length=50)),
                ('stipend', models.DecimalField(decimal_places=2, max_digits=10)),
                ('working_duration', models.IntegerField()),
                ('interview_date', models.DateField()),
                ('joining_date', models.DateField()),
                ('selection_status', models.CharField(choices=[('Selected', 'Selected'), ('Waiting List', 'Waiting List')], max_length=50)),
                ('working_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('father_occupation', models.CharField(max_length=50)),
                ('mother_occupation', models.CharField(max_length=50)),
                ('blood_group', models.CharField(max_length=3)),
                ('current_address', models.TextField()),
                ('permanent_address', models.TextField()),
                ('school_10th_name', models.CharField(max_length=100)),
                ('percentage_10th', models.DecimalField(decimal_places=2, max_digits=5)),
                ('year_of_passing_10th', models.IntegerField()),
                ('school_12th_name', models.CharField(max_length=100)),
                ('percentage_12th', models.DecimalField(decimal_places=2, max_digits=5)),
                ('year_of_passing_12th', models.IntegerField()),
                ('ug_college_name', models.CharField(max_length=100)),
                ('ug_course', models.CharField(max_length=50)),
                ('ug_degree', models.CharField(max_length=50)),
                ('ug_cgpa', models.DecimalField(decimal_places=2, max_digits=4)),
                ('ug_year_of_passing', models.IntegerField()),
                ('pg_college_name', models.CharField(blank=True, max_length=100)),
                ('pg_course', models.CharField(blank=True, max_length=50)),
                ('pg_degree', models.CharField(blank=True, max_length=50)),
                ('pg_cgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('pg_year_of_passing', models.IntegerField(blank=True, null=True)),
                ('previous_company', models.CharField(blank=True, max_length=100)),
                ('job_title', models.CharField(blank=True, max_length=50)),
                ('years_of_experience', models.IntegerField(blank=True, null=True)),
                ('resume_upload', models.BinaryField(null=True)),
                ('linkedin', models.URLField(blank=True)),
            ],
        ),
    ]
