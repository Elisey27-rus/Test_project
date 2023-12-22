from django.db import models
from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    descriptions = models.TextField(null=False, blank=True)

    def get_absolute_url(self):
            return reverse('item_details', args=[str(self.id)])

    
