from django.contrib.auth import get_user_model
from django.db import models


class CategoryQuerySet(models.query.QuerySet):
    def for_user(self, user):
        return self.filter(user=user)


class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    objects = CategoryQuerySet.as_manager()

    def __str__(self):
        return self.name
