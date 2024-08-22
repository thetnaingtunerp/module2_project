from django.urls import path
from .views import *
from . import views
app_name = 'myapp'
urlpatterns = [
    path('DashboardView/', DashboardView.as_view(), name='DashboardView'),
    path('AdminTemplate/', AdminTemplate.as_view(), name='AdminTemplate'),

    path('itemcreateview/', itemcreateview.as_view(), name='itemcreateview'),
    # Backend 

    path('itemview/', itemview.as_view(), name='itemview'),
    path('categoryview/', categoryview.as_view(), name='categoryview'),
    path('orderlistview/', orderlistview.as_view(), name='orderlistview'),

    # Frontend 
    path('', shopview.as_view(), name='shopview'),
    path('productdetail/<int:pk>/', productdetail.as_view(), name='productdetail'),
    path('addtocart/', addtocart.as_view(), name='addtocart'),
    path('cartview/', cartview.as_view(), name='cartview'),
    path('cart_change_qty/', cart_change_qty.as_view(), name='cart_change_qty'),
    path('send_order_to_admin/', send_order_to_admin.as_view(), name='send_order_to_admin'),
    
]