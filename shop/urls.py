from django.urls import path
from shop.views import all_items, get_item, get_item_page

urlpatterns = [
    path('<int:shop>/categories/<int:category>', all_items),
    path('<int:shop>/categories/<int:category>?<int:page>', get_item_page),
    path('<int:shop>/categories/<int:category>/<int:item>', get_item),
    # path('categories/', endpoint),
]