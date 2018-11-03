# Generated by Django 2.1.1 on 2018-11-03 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='moves',
            field=models.CharField(default='DEFAULT MOVES', max_length=1000),
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.CharField(default='DEFAULT DESCRIPTION', max_length=1000),
        ),
    ]