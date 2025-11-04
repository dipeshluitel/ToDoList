from django.db import models

# Create your models here.
class To_do_list(models.Model):
    listed = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.listed
    