# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Reading(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    series_id = models.DecimalField(max_digits=18, decimal_places=8, blank=True, null=True)
    ttr = models.FloatField()
    location_id = models.IntegerField(blank=True, null=True)
    device_address = models.IntegerField()
    data_address = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_reading'
    # end of Meta
# end of Reading class

class Emissivity(models.Model):
    reading = models.ForeignKey(Reading, models.DO_NOTHING)
    value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tbl_emissivity'
    # end of Meta
# end of Emissivity class

class Temperature(models.Model):
    reading = models.ForeignKey(Reading, models.DO_NOTHING)
    kelvin = models.FloatField()
    celcius = models.FloatField(blank=True, null=True)
    fahrenheit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_temperature'
    # end of Meta
# end of Temperature class
