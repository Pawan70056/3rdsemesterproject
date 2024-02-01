# Generated by Django 5.0 on 2024-02-01 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_course_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='course.instructor'),
            preserve_default=False,
        ),
    ]
