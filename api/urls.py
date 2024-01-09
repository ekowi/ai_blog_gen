from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_data, name="api_home")
]