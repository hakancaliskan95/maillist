from django.db import models


class mails(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

