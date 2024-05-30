from django.db import models
from uuid import uuid4
import hashlib




def upload_image(instance, filename):
    hash_instance = hashlib.sha256(str(instance.id).encode())
    hashed_filename = hash_instance.hexdigest() + '-' + filename
    return hashed_filename

# Create your models here.
class RemedyOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    manufacturer = models.CharField(max_length=150)
    value = models.FloatField()
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)

    def __str__(self):
        return self.name.upper()