# Generated by Django 5.0 on 2023-12-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManyToManyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='students',
            field=models.ManyToManyField(related_name='teachers', related_query_name='teacher', to='ManyToManyApp.student'),
        ),
    ]
