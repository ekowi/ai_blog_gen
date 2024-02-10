from django.contrib import admin
from .models import BlogPost, Additionals, Product

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Additionals)
admin.site.register(Product)
