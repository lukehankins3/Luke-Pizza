from django.db import models

# Create your models here.

#Define a model Pizza with a field called pizza_name 
#This field is the name of the pizza such as Hawaiian, etc.
#Define a model called Topping with fields called pizza and 
# topping_name. The pizza field should be a foreign key to 
# the Pizza model, and topping_name should include sausage, etc.

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    #picture = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.pizza_name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField()

    def __str__(self):
        return self.topping_name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment
