from django.db import models

# Create your models here.


class Customer(models.Model):
<<<<<<< HEAD
    name= models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null= True)

    def __str__(self):
        return self.name
class Tag(models.Model):
    name= models.CharField(max_length=200,null=True)



    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
            ('Indoor', 'Indoor'),
            ('Out Door', 'Out Door'),)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
	
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('Out for delivery', 'Out for delivery'),
            ('Delivered', 'Delivered'),)
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
=======
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null= True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    data_created = models.DateTimeField(auto_now_add=True, null= True)

class Order(models.Model):
    STATUS = (
        ('Fending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Deliered','Deliered'),
    )

    #customer = 
    #product = 
    data_created = models.DateTimeField(auto_now_add=True, null= True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
>>>>>>> 86e89b52715afcce1810ecb90e5ad174f08409cd
