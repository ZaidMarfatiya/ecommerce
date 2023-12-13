from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class Customer(models.Model):
    name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, validators=[
        MinValueValidator(0.01), MaxValueValidator(25)])

    def __str__(self):
        return self.name


class Order(models.Model):
    order_number = models.CharField(max_length=10, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    address = models.TextField()

    @property
    def order_items(self):
        return self.orderitem_set.all()

    def create_order_number(self):
        last_order = Order.objects.order_by('-id').first()
        if last_order:
            order_number = last_order.id + 1
        else:
            order_number = 1
        return f'ORD{str(order_number).zfill(5)}'

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self.create_order_number()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order_number} - {self.customer.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        total_weight = 0
        order_items = OrderItem.objects.filter(order=self.order)

        for item in order_items:
            total_weight += item.product.weight * item.quantity

        if total_weight > 150:
            raise ValidationError('Order exceeds maximum weight limit')

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.order.order_number}"

