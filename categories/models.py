from django.db import models
from user.models import User

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    categories = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.categories