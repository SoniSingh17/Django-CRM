from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return f"First Name : {self.first_name}\n Last Name : {self.last_name}"

