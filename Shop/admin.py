from django.contrib import admin
from Shop.models import Animelist, Hoodies, Joggers, Facemasks, Cosplay, Backpacks, Rings, Contact

class HoodiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class JoggersAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class FacemasksAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class CosplayAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class BackpacksAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class RingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class AnimelistAdmin(admin.ModelAdmin):
    list_display = ('rank', 'name', 'rating')



# Register your models here.
admin.site.register(Contact)
admin.site.register(Hoodies, HoodiesAdmin)
admin.site.register(Joggers, JoggersAdmin)
admin.site.register(Facemasks, FacemasksAdmin)
admin.site.register(Cosplay, CosplayAdmin)
admin.site.register(Backpacks, BackpacksAdmin)
admin.site.register(Rings, RingsAdmin)
admin.site.register(Animelist, AnimelistAdmin)