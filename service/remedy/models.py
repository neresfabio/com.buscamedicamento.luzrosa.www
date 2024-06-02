from django.db import models
from uuid import uuid4    

class LocationUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city.upper()} + {self.region.upper()}"

class ExternalRemedyData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    snippet = models.TextField()
    link = models.URLField()
    image = models.CharField(max_length=355)
    location = models.ForeignKey(LocationUser, on_delete=models.PROTECT, related_name='locations')

    def __str__(self):
        return self.title