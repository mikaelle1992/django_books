from django.db import models
from uuid import uuid4

def upload_to_file(instance, filename):
    return f'{instance.id_book}-{filename}'

# Create your models here.
class Books(models.Model):
    
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=225)
    outhor = models.CharField(max_length=225)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    imagen =models.ImageField(upload_to=upload_to_file, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    