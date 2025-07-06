from django.contrib.auth import get_user_model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = get_user_model()

    def __str__(self):
        return self.name