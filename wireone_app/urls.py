
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('get_price',views.get_price,name='index'),
    path('get_price_by_id',views.get_price_by_id,name='get_price_by_id'),
    path('new_DBP',views.new_DBP,name='new_DBP'),
    path('new_TMF',views.new_TMF,name='new_TMF'),
    path('new_Price',views.new_Price,name='new_Price'),
    

]
