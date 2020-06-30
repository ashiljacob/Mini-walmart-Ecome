from django.db import models


# Create your models 
CATEGORY_CHOICES = [
    ('U', 'Pulses'),
    ('O', 'Oil'),
    ('F', 'Flour'),
    ('V', 'Vegetable')]

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantityofproduct = models.IntegerField(blank=True, null=True)
    quantityAvailable = models.IntegerField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=1)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedDate= models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class BillItem(models.Model):
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.item

    def get_total_item_price(self):
        return self.quantity*self.price


    
  