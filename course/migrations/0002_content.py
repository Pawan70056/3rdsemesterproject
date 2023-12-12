# Generated by Django 5.0 on 2023-12-12 11:41

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('text', 'Text'), ('pdf', 'PDF')], default='text', max_length=4)),
                ('text_content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='pdf_contents/')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='course.chapter')),
            ],
        ),
    ]
