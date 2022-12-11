# Generated by Django 4.1.3 on 2022-12-01 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hamakua_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basin', models.CharField(max_length=2)),
                ('pitfallTrapNum', models.IntegerField(max_length=10)),
                ('taxonmicResolution', models.CharField(max_length=100)),
                ('specieCount', models.IntegerField()),
            ],
            options={
                'db_table': 'Hamakua_Data',
            },
        ),
    ]
