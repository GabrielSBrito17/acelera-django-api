from django.db import models

# Create your models here.
class Category(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Products(models.Model):
    user_id = models.ForeignKey(Client, related_name='user_id', on_delete=models.CASCADE)
    name_product = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.URLField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name_product
