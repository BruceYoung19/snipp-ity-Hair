from django.db import models

class user(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()
    account_created = models.TimeField(auto_now_add=True)
    Member = models.BooleanField(default=True)

#class haircuts(Models.models):
#   name 
#   cost
#   description

#class orders(Models.models):
#  orderNumber
#  cost
#  date

# class business(Models.models):
#   name = models.CharField(max_Length=50)
#   
#   self __str__(self):
#       return self.name 
#
#



