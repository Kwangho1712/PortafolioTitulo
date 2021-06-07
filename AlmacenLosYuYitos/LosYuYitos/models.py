# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allo w Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
 
class Proveedor(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=99)
    telefono = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=99, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    rubro = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    run = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=99)
    edad = models.BigIntegerField(blank=True, null=True)
    fiar = models.BooleanField()
    fiado_id_fiado = models.ForeignKey('Fiado', on_delete=models.CASCADE, db_column='fiado_id_fiado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'
    
    def __str__(self):
        return self.run


class Fiado(models.Model):
    id_fiado = models.AutoField(primary_key=True)
    monto_fiado = models.FloatField(blank=True, null=True)
    fecha_fiado = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fiado'

    def __str__(self):
        return self.id_fiado

class Producto(models.Model):
    cod_producto = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio_compra = models.FloatField()
    precio_venta = models.FloatField()
    tipo_prod_id_tipo_prod = models.ForeignKey('TipoProducto', on_delete=models.CASCADE, db_column='tipo_prod_id_tipo_prod', blank=True, null=True)
    fam_prod_id_fam_prod = models.ForeignKey('FamiliaProducto', on_delete=models.CASCADE, db_column='fam_prod_id_fam_prod', blank=True, null=True)
    stock_actual = models.FloatField()
    stock_critico = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'

    def __str__(self):
        return self.nombre


class FamiliaProducto(models.Model):
    id_familia_producto = models.AutoField(primary_key=True)
    dsc_familia_producto = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'familia_producto'
    
    def __str__(self):
        return self.dsc_familia_producto


class TipoProducto(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    dsc_tipo_producto = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_producto'

    def __str__(self):
        return self.dsc_tipo_producto