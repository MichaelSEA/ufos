from django.db import models


class Sighting(models.Model):
    sighting_id = models.IntegerField()
    occurred_at = models.DateTimeField()
    city = models.CharField(db_index=True, max_length=512)
    state = models.CharField(max_length=2, null=True, blank=True)
    country = models.CharField(max_length=2, null=True, blank=True)
    shape = models.CharField(db_index=True, max_length=512)
    duration_seconds = models.FloatField()
    duration_text = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    reported_on = models.DateField()
    latitude = models.DecimalField(db_index=True, decimal_places=7, max_digits=10)
    longitude = models.DecimalField(db_index=True, decimal_places=7, max_digits=10)


