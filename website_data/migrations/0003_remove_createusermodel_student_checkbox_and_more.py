# Generated by Django 4.0.6 on 2023-07-03 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_data', '0002_alter_createusermodel_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createusermodel',
            name='student_checkbox',
        ),
        migrations.RemoveField(
            model_name='createusermodel',
            name='teacher_checkbox',
        ),
    ]