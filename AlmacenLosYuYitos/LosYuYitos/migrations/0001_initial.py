# Generated by Django 3.2.3 on 2021-05-25 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('run', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=99)),
                ('edad', models.BigIntegerField(blank=True, null=True)),
                ('fiar', models.BooleanField()),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fiado',
            fields=[
                ('id_fiado', models.AutoField(primary_key=True, serialize=False)),
                ('monto_fiado', models.FloatField(blank=True, null=True)),
                ('fecha_fiado', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fiado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=99)),
                ('telefono', models.CharField(blank=True, max_length=13, null=True)),
                ('email', models.CharField(blank=True, max_length=99, null=True)),
                ('direccion', models.CharField(blank=True, max_length=60, null=True)),
                ('rubro', models.CharField(blank=True, max_length=90, null=True)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
    ]