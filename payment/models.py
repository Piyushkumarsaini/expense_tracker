from django.db import models
from user.models import User


class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    payment_method = models.CharField(max_length=100)

    def __str__(self):
        return self.payment_method