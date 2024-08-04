import uuid
from django.db import models

# Create your models here.
class creationData(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    owner_id = models. CharField(default=None)
    price = models.FloatField(default=0.0)
    description = models.TextField(max_length=1000)
    # image = models.ImageField(upload_to='images/', default=None)

    def __str__(self):
        return self.owner_id