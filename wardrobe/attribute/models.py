from django.db import models

class Color(models.Model):
    color = models.CharField("Color", max_length=50)

    def __str__(self):
        return self.color
    
class Brand(models.Model):
    brand = models.CharField("Brand", max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.brand

class ClothType(models.Model):
    cloth_type = models.CharField("ClothType", max_length=100)

    def __str__(self):
        return self.cloth_type

class Season(models.Model):
    season = models.CharField("Season", max_length=100)

    def __str__(self):
        return self.season

class Size(models.Model):
    size = models.CharField("Size", max_length=50)

    def __str__(self):
        return self.size