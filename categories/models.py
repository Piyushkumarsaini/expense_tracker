from django.db import models

class Category(models.Model):
    categories = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.categories