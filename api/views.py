# views.py
from django.http import JsonResponse
from blog_generator.models import Product, Additionals


def get_all_product(request):
    data = Product.objects.values()  # Retrieve all data from the database
    return JsonResponse(list(data), safe=False)


def get_all_additionals(request):
    data = Additionals.objects.values()
    return JsonResponse(list(data), safe=False)


def product_detail(request):
    try:
        products = Product.objects.all()

        # List to store combined product and additional data
        combined_data_list = []

        # Iterate over each product
        for product in products:
            # Serialize product data
            product_data = {
                "id": product.id,
                "title": product.title,
                "description": product.description,
                "price": str(product.price),
                "category": product.category,
                "url": product.url,
                "is_active": product.is_active,
            }

            # Serialize associated additional data
            additional_data_list = []
            for additional in product.additionals.all():
                additional_data_list.append(
                    {
                        "id": additional.id,
                        "title": additional.title,
                        "description": additional.description,
                    }
                )

            # Combine product and additional data
            combined_data = {
                "product": product_data,
                "additional_data": additional_data_list,
            }

            # Add combined data to the list
            combined_data_list.append(combined_data)

        return JsonResponse({"products": combined_data_list})
    except Product.DoesNotExist:
        return JsonResponse({"error": "Products not found"}, status=404)
