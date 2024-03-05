from django.db import models

# Create your models here.

class Product_Catagory(models.Model):
    Product_Catagory_id=models.IntegerField(primary_key=True)
    Product_Catagory_name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.Product_Catagory_name

class Product(models.Model):
    product_catagory_id=models.ForeignKey(Product_Catagory,on_delete=models.CASCADE)
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_brand=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.product_name