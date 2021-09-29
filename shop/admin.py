from django.contrib import admin

from .models import Item, ItemImage

class PostImageAdmin(admin.StackedInline):
    model = ItemImage

@admin.register(Item)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Item

@admin.register(ItemImage)
class PostImageAdmin(admin.ModelAdmin):
    pass