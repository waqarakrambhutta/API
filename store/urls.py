from django.urls import path
from . import views

urlpatterns=[
    path('products/',views.product_list),
    # path('product/<id>/',views.product_detail)
    #this will also works if we put letter a or anything which is not in rules.
    path('products/<int:id>/',views.product_detail),
    path('collection/<id>/',views.Collection_id),
    path('collection/',views.Collection_list),
    ]