from django.db import models

class User(models.Model):
    city = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.city