from django.contrib import admin

# Register your models here.

from .models import Car, OfferImage


class OfferImageAdmin(admin.StackedInline):
    model = OfferImage

@admin.register(Car)
class OfferAdmin(admin.ModelAdmin):
    inlines = [OfferImageAdmin]

    class Meta:
        model = Car

@admin.register(OfferImage)
class OfferImageAdmin(admin.ModelAdmin):
    pass