from django.urls import path
from .views import *
from . import views
app_name = 'myapp'
urlpatterns = [
    path('DashboardView/', DashboardView.as_view(), name='DashboardView'),
    path('AdminTemplate/', AdminTemplate.as_view(), name='AdminTemplate'),

    path('itemcreateview/', itemcreateview.as_view(), name='itemcreateview'),

    path('itemview/', itemview.as_view(), name='itemview'),
]