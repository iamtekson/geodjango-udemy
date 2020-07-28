from django.db import models
from django.contrib.gis.db import models as gis_models


# Create your models here.
class Jamoat(models.Model):
    object_id = models.AutoField(primary_key=True)
    geom = gis_models.MultiPolygonField(srid=32642, blank=True, null=True)
    objectid = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    region = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    district = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    id = models.CharField(max_length=50, blank=True, null=True)
    # Field renamed because it ended with '_'.
    cadastral_field = models.CharField(
        db_column='cadastral_', max_length=50, blank=True, null=True)
    type = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    standard_n = models.CharField(max_length=50, blank=True, null=True)
    alternativ = models.CharField(max_length=50, blank=True, null=True)
    population = models.CharField(max_length=50, blank=True, null=True)
    shape_leng = models.DecimalField(
        max_digits=15, decimal_places=7, blank=True, null=True)
    shape_area = models.DecimalField(
        max_digits=15, decimal_places=7, blank=True, null=True)
    district_e = models.CharField(max_length=30, blank=True, null=True)
    jamoat_eng = models.CharField(max_length=30, blank=True, null=True)
    jambi_name = models.CharField(max_length=22, blank=True, null=True)
    altern_eng = models.CharField(max_length=22, blank=True, null=True)
    name_rg = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jamoat'
