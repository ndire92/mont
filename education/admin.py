from django.contrib import admin

from education.models import DimEduc_Equipements, Visiteur, DimEduc_Gouvernance, DimEduc_Perfomance, DimEduc_Personnel, DimEduc_Access

# Register your models here.

admin.site.register(DimEduc_Equipements)
admin.site.register(DimEduc_Gouvernance)
admin.site.register(DimEduc_Perfomance)
admin.site.register(DimEduc_Personnel)
admin.site.register(DimEduc_Access)
admin.site.register(Visiteur)
