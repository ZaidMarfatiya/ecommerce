from django.urls import path
from .views import (
    CustomerList,
    CustomerDetail,
    ProductList,
    OrderList,
    OrderDetail
)

urlpatterns = [
    path('customers/', CustomerList.as_view()),
    path('customers/<int:pk>/', CustomerDetail.as_view()),
    path('products/', ProductList.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
]

