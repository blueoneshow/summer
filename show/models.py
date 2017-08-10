from django.db import models
from django.utils import timezone

class Record(models.Model):
        seconds = models.IntegerField(default=0)
        publication_date = models.DateTimeField(default=timezone.now)