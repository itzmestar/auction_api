from django.urls import path
from . import views
urlpatterns = [
    path('item/', views.ItemList.as_view(), name='items'),
    path('item/<int:pk>/', views.ItemDetails.as_view(), name='item'),
    path('bid/', views.BidCreate.as_view(), name='bid'),
]