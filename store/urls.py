from django.urls import path,include
from . import views
from rest_framework_nested import routers
from rest_framework_nested.routers import DefaultRouter,NestedDefaultRouter

router = DefaultRouter()
router.register('cart',views.CartViewset)
router.register('cartitems',views.CartItemViewset)

cart_router = NestedDefaultRouter(router,'cart',lookup = 'cart')
cart_router.register('items',views.CartItemVeiwSet,basename='cart-item-router')

urlpatterns = router.urls + cart_router.urls

# urlpatterns =[
#     path('',include(router.urls)),
#     # path('cartitem/',views.CartItem_list)
# ]



















# from rest_framework_nested import routers

# router = routers.DefaultRouter()
# router.register('products',views.ProductViewset,basename='product')
# router.register('collections',views.CollectionViewSets)

# products_router = routers.NestedDefaultRouter(router,'products',lookup='product')
# products_router.register('reviews',views.ReviewViewset ,basename='product-reviews')

# urlpatterns = router.urls + products_router.urls
# urlpatterns =[
#     path('',include(router.urls)),
#     path('',include(products_router.urls)),
# ]

# urlpatterns=[
    # path('products/',views.ProductList.as_view()),
    # path('products/<int:pk>/',views.ProductDetail.as_view()),
    #this will also works if we put letter a or anything which is not in rules.
    # path('products/<int:id>/',views.product_detail),
    # path('collections/',views.CollectionList.as_view()),
    # path('collections/<int:pk>/',views.CollectionDetail.as_view()),
    # path('collection/<int:id>/',views.collection_detail,name='collection-detail'),
    # path('collection/',views.collection_list)
    # ]