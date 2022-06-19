from tkinter import CASCADE
from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Stock(models.Model):
    ticker = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    value = models.DecimalField(max_digits=14, decimal_places=4)
    goal = models.DecimalField(max_digits=5, decimal_places=2)
    actual = models.DecimalField(max_digits=5, decimal_places=2)

    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticker

