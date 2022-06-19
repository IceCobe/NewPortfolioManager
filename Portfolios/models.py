from tkinter import CASCADE
from django.db import models


class Portfolio(models.Model):
    name = models.CharField()

class Stock(models.Model):
    ticker = models.CharField()
    name = models.CharField()
    quantity = models.PositiveIntegerField()
    value = models.DecimalField(decimal_places=2)
    goal = models.DecimalField()
    actual = models.DecimalField()

    portfolio = models.ForeignKey(Portfolio, on_delete=CASCADE)

