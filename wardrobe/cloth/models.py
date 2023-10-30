from django.db import models
from attribute.models import Color
from attribute.models import Brand
from attribute.models import ClothType
from attribute.models import Season
from attribute.models import Size

class Cloth(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    cloth_type = models.ForeignKey(ClothType, on_delete=models.PROTECT)
    colors = models.ManyToManyField(Color)
    season = models.ManyToManyField(Season)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    details = models.CharField("Details", blank=True, max_length=300)
    is_usable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
