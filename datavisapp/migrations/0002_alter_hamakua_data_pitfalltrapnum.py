# Generated by Django 4.1.3 on 2022-12-01 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datavisapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamakua_data',
            name='pitfallTrapNum',
            field=models.IntegerField(),
        ),
    ]
