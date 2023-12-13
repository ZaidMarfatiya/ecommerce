# Ecommerce Project

This Django REST API serves as the backend for an ecommerce store, providing functionalities to manage customers, products, and orders.

## Features

- **Customers CRUD:** Create, Read, Update, and Delete customer information.
- **Products CRUD:** Manage product details, including name and weight.
- **Orders CRUD:** Create, Read, and Update order information, including automatically generated order numbers.
- **Calculate Order Total Weight:** Dynamically calculate the total weight of an order based on its items.
- **Validate Item Weights:** Ensure that items in an order do not exceed weight limits.
- **Filter Orders:** Filter orders based on customers or products.
- **Swagger/OpenAPI Documentation:** Explore API documentation using Swagger/OpenAPI.

## Models

### Customer

- `id`
- `name`
- `contact_number`
- `email`

### Product

- `id`
- `name`
- `weight`

### Order

- `id`
- `order_number` (auto-generated)
- `customer` (Foreign Key to Customer)
- `order_date`
- `address`

### OrderItem

- `id`
- `order` (Foreign Key to Order)
- `product` (Foreign Key to Product)
- `quantity`

## Installation

To get started, follow these steps:

1. Create and activate a virtual environment.
2. Install required dependencies using `pip install -r requirements.txt`.
3. Run database migrations: `python manage.py migrate`.
4. Create a superuser account: `python manage.py createsuperuser`.
5. Start the development server: `python manage.py runserver`.

## API Endpoints

### Customers

- **GET, POST** `/api/customers/`
- **GET, PUT, DELETE** `/api/customers/{id}`

### Products

- **GET, POST** `/api/products/`

### Orders

- **GET, POST** `/api/orders/`
- **GET, PUT** `/api/orders/{id}`

### Filter Orders

- Filter orders by customer or products.

## Swagger API Docs

Browse the API documentation at `http://127.0.0.1:8000/docs/` to explore and interact with the available endpoints.

