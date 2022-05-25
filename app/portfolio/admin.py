from django.contrib import admin
from.models import *


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass