# Generated by Django 4.0.6 on 2023-07-10 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_data', '0013_testfilemodel_lastname_testfilemodel_pdf_file1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testfilemodel',
            name='firstname',
            field=models.CharField(default='___', max_length=100),
        ),
        migrations.AlterField(
            model_name='testfilemodel',
            name='lastname',
            field=models.CharField(default='___', max_length=100),
        ),
        migrations.AlterField(
            model_name='testfilemodel',
            name='pdf_file1',
            field=models.FileField(default='No File Chosen', upload_to=''),
        ),
    ]