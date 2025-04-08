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


class Income(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    category_id = models.ForeignKey(IncomeCategory,on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=20)
    amount = models.IntegerField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True,null=True)

    def __str__(self):
        return self.user_id

    
class ExpenseCategory(models.Model):
    expense_category = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.expense_category
    

class PatmentMethod(models.Model):
    payment_method = models.CharField(max_length=20)

    def __str__(self):
        return self.payment_method
    

class Expense(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(ExpenseCategory,on_delete=models.SET_NULL, null=True)
    payment_method_id = models.ForeignKey(PatmentMethod, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=20)
    amount = models.IntegerField()
    description = models.TextField(blank=True,null=True, default="")
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True,null=True)


    def __str__(self):
        return self.user_id


    
class Budget(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    category_id = models.ForeignKey(ExpenseCategory,on_delete=models.CASCADE)
    limit = models.IntegerField()

    def __str__(self):
        return self.user_id