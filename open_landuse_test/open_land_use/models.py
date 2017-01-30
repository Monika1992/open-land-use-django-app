from __future__ import unicode_literals
from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db import models as geo_models
from django.db import models


class Municipality_area(models.Model):
    id = models.IntegerField(primary_key=True, serialize=True)
    geom = geo_models.GeometryField()
    hilucs_land_use_value = models.IntegerField(default=0)
    original_land_use_value = models.TextField()
    geometry_source = models.TextField()
    attribute_source = models.TextField()
    municipal_code = models.TextField()
    validfrom = models.DateField()
    validto = models.DateField()

# class OLU_area(models.Model):

