from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=30, verbose_name="Company/Fund")
    ticker = models.CharField(max_length=5, verbose_name="Ticker")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Price")
    holdings = models.PositiveIntegerField(verbose_name="Holdings")
    equity = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Equity")
    goal = models.PositiveIntegerField(verbose_name="Goal Percentage")
    current = models.PositiveIntegerField(verbose_name="Current Percentage")