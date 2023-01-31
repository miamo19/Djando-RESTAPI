from django.db import models

class Drink(models.Model):
    """
    name: Drink
    description: This class keep record on drink
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name +" " + self.description
