# Generated by Django 4.1.3 on 2022-12-09 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datavisapp', '0005_alter_hamakua_data_basin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hamakua_After_Disking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basin', models.CharField(max_length=999)),
                ('taxonomicResolution', models.CharField(max_length=100)),
                ('specieCount', models.IntegerField()),
            ],
            options={
                'db_table': 'Hamakua_After_Disking',
            },
        ),
    ]
