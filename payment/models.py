from django.db import models


class PaymentMethod(models.Model):
    payment_method = models.CharField(max_length=100)

    def __str__(self):
        return self.payment_method