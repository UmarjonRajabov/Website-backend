from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    picture = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=255)

    def __str__(self):
        return self.title