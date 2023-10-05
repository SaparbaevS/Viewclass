from django.contrib import admin

from shop.models import Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", 'slug', 'price',)
    # list_display_links = ('title', 'slug', 'price')
    list_filter = ('price', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title', )}

    actions_on_top = True
    actions_on_bottom = False

    # date_hierarchy = 'product_date'
    # empty_value_display = '~empty~'
    #
    # fields = (("title", 'slug'), ('price', 'product_date'))

    ordering = ('price', )



admin.site.register(Product, ProductAdmin)
