from django.db import models
from django.contrib.auth.models import User

class WeightEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    # def __str__(self):
    #     return f"{self.user.username} - {self.date} - {self.weight}"
