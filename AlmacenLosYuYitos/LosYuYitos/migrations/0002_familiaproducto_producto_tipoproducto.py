# Generated by Django 3.2.3 on 2021-06-05 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LosYuYitos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamiliaProducto',
            fields=[
                ('id_familia_producto', models.AutoField(primary_key=True, serialize=False)),
                ('dsc_familia_producto', models.CharField(blank=True, max_length=999, null=True)),
            ],
            options={
                'db_table': 'familia_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('cod_producto', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio_compra', models.FloatField()),
                ('precio_venta', models.FloatField()),
                ('stock_actual', models.FloatField()),
                ('stock_critico', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id_tipo_producto', models.AutoField(primary_key=True, serialize=False)),
                ('dsc_tipo_producto', models.CharField(blank=True, max_length=999, null=True)),
            ],
            options={
                'db_table': 'tipo_producto',
                'managed': False,
            },
        ),
    ]
