from django.db import models

# Create your models here.
class Finch(models.Model):
    # s_name is scientific name, just got lazy spelling that out
    s_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.s_name
