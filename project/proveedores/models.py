from django.db import models

class proveedores(models.Model):
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
