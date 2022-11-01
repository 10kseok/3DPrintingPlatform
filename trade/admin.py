from django.contrib import admin

from .models import Estimate, Bid, Trade

admin.site.register(Estimate)
admin.site.register(Bid)
admin.site.register(Trade)