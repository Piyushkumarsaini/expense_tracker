from django.db import models
from payment.models import PaymentMethod
from categories.models import Category
from user.models import User



class Income(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=10)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    description = models.TextField(blank=True,null=True, default="")
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True,null=True)

    def __str__(self):
        return str(self.user_id)



class Expense(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=10)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    description = models.TextField(blank=True,null=True, default="")
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True,null=True)


    def __str__(self):
        return str(self.user_id)