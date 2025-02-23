from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(max_length = 200)

    def __str__(self):
        return self.full_name
# Compare this snippet from contactlist/urls.py: