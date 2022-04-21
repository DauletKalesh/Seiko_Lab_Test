# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from shop.serializers import ItemSerializers
from shop.models import Categories,Items,Shops
from rest_framework.views import Response

# Create your views here.

def all_items(request, shop, category):
    try:
        obj = Categories.objects.filter(shop_id=int(shop), id=int(category))
        cat = int(category)
    except:
        obj = None
    print(cat)

    if request.method == 'GET':
        items = Items.objects.all()
        if obj:
            data = items.filter(category_id=cat)
            serializer = ItemSerializers(data, many=True)
            return JsonResponse(serializer.data, safe=False)
        return Response({'error': 'У вас нет такого категории или магазина.'})
    elif request.method == 'POST':
        serializer = ItemSerializers(data=eval(request.body), many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False, status=404)
    
def get_item(request, shop, category, item):
    try:
        obj = Categories.objects.filter(shop_id=int(shop), id=int(category))
        cat = int(category)
    except:
        obj = None
    print(cat)

    if request.method == 'GET':
        items = Items.objects.all()
        if obj:
            data = items.filter(category_id=cat, id=int(item))
            serializer = ItemSerializers(data, many=True)
            return JsonResponse(serializer.data, safe=False)
        return Response({'error': 'У вас нет такого категории или магазина.'})

    elif request.method == 'PUT':
        serializer = ItemSerializers(data=eval(request.body), many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False, status=404)

def get_item_page(request, shop, category, page):
    try:
        obj = Categories.objects.filter(shop_id=int(shop), id=int(category))
        cat = int(category)
    except:
        obj = None
    print(cat)

    if request.method == 'GET':
        items = Items.objects.all()
        if obj:
            data = items.filter(category_id=cat)[(page-1)*5:page*5]
            serializer = ItemSerializers(data, many=True)
            return JsonResponse(serializer.data, safe=False)
        return Response({'error': 'У вас нет такого категории или магазина.'})