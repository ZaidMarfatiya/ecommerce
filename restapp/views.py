from rest_framework import generics
from restapp.models import Customer, Product, Order
from restapp.serializers import CustomerSerializer, ProductSerializer, \
    OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, CharFilter


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderFilter(FilterSet):
    customer = CharFilter(field_name='customer__name')
    products = CharFilter(field_name='orderitem__product__name', method='filter_products')

    def filter_products(self, queryset, name, value):
        products_list = value.split(',')
        return queryset.filter(orderitem__product__name__in=products_list)

    class Meta:
       model = Order
       fields = []


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter


class OrderDetail(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

