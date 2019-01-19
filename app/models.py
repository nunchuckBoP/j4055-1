# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime

class Series(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=18, decimal_places=8)

    @property
    def time(self):
        return datetime.fromtimestamp(self.id).strftime('%c')
    # end time

    @property
    def duration(self):
        reading_data = Reading.objects.filter(series_id=self.pk)
        time = 0.0
        for i in reading_data:
            time = time + i.ttr
        # end for
        return time
    # end duration

    @property
    def reading_count(self):
        return Reading.objects.filter(series_id=self.pk).count()
    # end reading_count

    def __str__(self):
        return self.time
    # end __str__()

    @property
    def max_object_temp(self):
        reading_data = Reading.objects.filter(series_id=self.id).filter(name='object')
        max_temp = 0.0
        for a_reading in reading_data:
            temp_query = a_reading.temperature
            if temp_query.__len__() > 0:
                if max_temp < temp_query[0].kelvin:
                    max_temp = temp_query[0].kelvin
                # end if
            # end if
        # end for
        return max_temp
    # end max_object_temp

    @property
    def max_ttr(self):
       reading_data = Reading.objects.filter(series_id=self.id)
       max_ttr = 0.0
       for i in reading_data:
           if max_ttr < i.ttr:
               max_ttr = i.ttr
           # end if
       # end for
       return max_ttr
    # end max_ttr

    class Meta:
        managed = False
        db_table = 'tbl_series'
    # end Meta
# end Series class


class Reading(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    series = models.ForeignKey(Series, models.DO_NOTHING, blank=True, null=True)
    ttr = models.FloatField()
    location_id = models.IntegerField(blank=True, null=True)
    device_address = models.IntegerField()
    data_address = models.IntegerField()

    @property
    def temperature(self):
        return Temperature.objects.filter(reading=self.pk)
    # end temperature

    @property
    def emissivity(self):
        return Emissivity.objects.filter(reading=self.pk)
    # end emissivity

    @property
    def type(self):
        # gets the type of the reading by looking
        # the other tables
        t_count = Temperature.objects.filter(reading=self.id).count()
        e_count = Emissivity.objects.filter(reading=self.id).count()
        if t_count > 0:
            return "temperature"
        elif e_count > 0:
            return "emissivity"
        else:
            return "unknown"
        # end if
    # end type

    def __str__(self):
        return str(self.ttr)
    # end __str__()

    class Meta:
        managed = False
        db_table = 'tbl_reading'
    # end Meta
# end Reading class


class Emissivity(models.Model):
    reading = models.ForeignKey(Reading, models.DO_NOTHING)
    value = models.FloatField()

    def __str__(self):
        return str(self.value)
    # end __str__()

    class Meta:
        managed = False
        db_table = 'tbl_emissivity'
    # end Meta
# end Emissivity class


class Temperature(models.Model):
    reading = models.ForeignKey(Reading, models.DO_NOTHING)
    kelvin = models.FloatField()
    celcius = models.FloatField(blank=True, null=True)
    fahrenheit = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.kelvin)
    # end __str__()

    class Meta:
        managed = False
        db_table = 'tbl_temperature'
    # end Meta
# end Temperature class
