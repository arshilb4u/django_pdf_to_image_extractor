# Generated by Django 2.2.12 on 2020-09-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='upload'),
        ),
    ]