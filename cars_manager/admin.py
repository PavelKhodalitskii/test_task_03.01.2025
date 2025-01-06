from django.contrib import admin

from .models import Brand, Car, Comment


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Brand._meta.fields]
    search_fields = ("name",)

@admin.register(Car)
class Car(admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.fields]
    search_fields = ("mark", "model")
    list_filter = ("year", "created_at", "updated_at")

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]
    search_fields = ("content", "model")
    list_filter = ("created_at",)