# Generated by Django 5.1.5 on 2025-01-20 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_course_owner_lesson_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='lesson_previews/'),
        ),
    ]
