from django.db import models

# Create your models here.

#point 2
class ImageUpload(models.Model):
    
    image_file=models.ImageField(upload_to="images")
