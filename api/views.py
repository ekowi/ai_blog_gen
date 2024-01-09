# views.py
from django.http import JsonResponse
from blog_generator.models import Product

def get_all_data(request):
    data = Product.objects.values()  # Retrieve all data from the database
    return JsonResponse(list(data), safe=False)
