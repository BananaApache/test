# Generated by Django 4.0.6 on 2023-07-10 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_data', '0011_remove_createusermodel_pdf_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testfilemodel',
            name='file',
        ),
        migrations.AddField(
            model_name='testfilemodel',
            name='firstname',
            field=models.CharField(default='firstname', max_length=100),
            preserve_default=False,
        ),
    ]
