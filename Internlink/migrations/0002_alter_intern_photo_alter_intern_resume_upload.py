# Generated by Django 5.1.2 on 2024-10-27 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Internlink', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intern',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='intern',
            name='resume_upload',
            field=models.FileField(null=True, upload_to='resumes/'),
        ),
    ]