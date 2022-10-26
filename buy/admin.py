from django.contrib import admin
#from trade.models import Estimate
from .models import Estimate

class EstimateAdmin(admin.ModelAdmin):
    search_fields = ['project_name']


admin.site.register(Estimate, EstimateAdmin)
