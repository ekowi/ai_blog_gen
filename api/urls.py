from django.urls import path
from . import views

urlpatterns = [
    path("product", views.get_all_product, name="api_product"),
    path("additionals", views.get_all_additionals, name="api_additionals"),
    path("product_details", views.product_details, name="product_details"),
]
