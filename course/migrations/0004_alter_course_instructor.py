# Generated by Django 5.0 on 2024-02-01 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_instructor_alter_course_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
