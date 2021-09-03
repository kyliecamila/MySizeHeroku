from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('상의', '상의'),
)
class Clothes(models.Model):
    category = models.CharField(max_length=255, choices = CATEGORY_CHOICES, default = '상의')
    name = models.CharField(max_length=255)
    photo = models.ImageField(null=True, blank = True, upload_to="images/")
    def __str__(self):
     return self.name

class Size(models.Model):
    name = models.ForeignKey("Clothes",on_delete= models.CASCADE, related_name = 'size' )
    sizeName = models.CharField(max_length=255)
    size1 = models.CharField(max_length=255)
    size2 = models.CharField(max_length=255, blank=True, null= True)
    size3 =  models.CharField(max_length=255, blank=True, null= True)
    size4 =  models.CharField(max_length=255, blank=True, null= True)
    def __str__(self):
     return str(self.name)

# class Photo(models.Model):
#     name = models.ForeignKey("Clothes", on_delete= models.CASCADE, related_name = 'photo')
#     # photo = models.ImageField(upload_to="static/images" , null= True, blank = True)
#     def __str__(self):
#      return str(self.name)