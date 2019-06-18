from django.db import models

from .choices import DEVICE_TYPE
from place.models import Place


class Device(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(choices=DEVICE_TYPE, max_length=1)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.name