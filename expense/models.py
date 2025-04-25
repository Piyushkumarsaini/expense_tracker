from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
    

class IncomeCategory(models.Model):
    income_category = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.income_category

class PaymentMethod(models.Model):
    payment_method = models.CharField(max_length=20)

    def __str__(self):
        return self.payment_method

class UserPaymentMethod(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.payment_method.payment_method
    

class Income(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    category = models.ForeignKey(IncomeCategory,on_delete=models.SET_NULL, null=True)
    payment_method = models.ForeignKey(UserPaymentMethod, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    description = models.TextField(blank=True,null=True, default="")
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True,null=True)

    def __str__(self):
        return str(self.user_id)

    
class ExpenseCategory(models.Model):
    expense_category = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.expense_category


class Expense(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    category = models.ForeignKey(IncomeCategory,on_delete=models.SET_NULL, null=True)
    payment_method = models.ForeignKey(UserPaymentMethod, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    description = models.TextField(blank=True,null=True, default="")
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True,null=True)


    def __str__(self):
        return str(self.user_id)


    
class Budget(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    category_id = models.ForeignKey(ExpenseCategory,on_delete=models.CASCADE)
    limit = models.IntegerField()

    def __str__(self):
        return self.user_id