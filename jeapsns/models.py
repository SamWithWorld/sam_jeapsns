from django.db import models
#table structure
class sns(models.Model):
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=140)
