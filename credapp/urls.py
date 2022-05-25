from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.addprod,name='addprod'),
    path('displayproduct',views.displayproduct,name='displayproduct'),
    path('showproduct',views.showproduct,name='showproduct'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('epdetails/<int:pk>',views.epdetails,name='epdetails'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('deleteproduct/<int:pk>',views.deleteproduct,name='deleteproduct')
]
