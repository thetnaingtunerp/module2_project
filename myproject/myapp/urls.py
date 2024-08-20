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

    # Frontend 
    path('', shopview.as_view(), name='shopview'),
    path('productdetail/<int:pk>/', productdetail.as_view(), name='productdetail'),
    path('addtocart/', addtocart.as_view(), name='addtocart'),
    
]