# views.py
from django.http import JsonResponse
from blog_generator.models import Product, Additionals


def get_all_product(request):
    data = Product.objects.values()  # Retrieve all data from the database
    return JsonResponse(list(data), safe=False)


def get_all_additionals(request):
    data = Additionals.objects.values()
    return JsonResponse(list(data), safe=False)
