```
marketplace/
├── manage.py
├── requirements.txt
├── .env
├── README.md
│
├── marketplace/                  # Core Django project config
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── urls.py
│   └── settings/
│       ├── __init__.py
│       ├── base.py
│       ├── dev.py
│       └── prod.py
│
├── apps/
│   ├── accounts/                 # User accounts (login/register)
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── templates/accounts/
│   │       ├── login.html
│   │       └── register.html
│   │
│   ├── products/                 # Marketplace products & categories
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── urls_api.py           # DRF router for product APIs
│   │   ├── views.py
│   │   ├── api/                  # Django REST Framework for products
│   │   │   ├── __init__.py
│   │   │   ├── serializers.py
│   │   │   └── views.py
│   │   └── templates/products/
│   │       ├── product_list.html
│   │       └── product_detail.html
│   │
│   ├── orders/                   # Orders & cart handling
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── urls_api.py           # DRF router for orders
│   │   ├── views.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── serializers.py
│   │   │   └── views.py
│   │   └── templates/orders/
│   │       ├── cart.html
│   │       └── checkout.html
│   │
│   └── payments/                 # Payment transactions
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── urls.py
│       ├── urls_api.py           # DRF router for payments
│       ├── views.py
│       ├── api/
│       │   ├── __init__.py
│       │   ├── serializers.py
│       │   └── views.py
│       └── templates/payments/
│           └── payment_success.html
│
├── static/                       # CSS, JS, and images
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/                        # User-uploaded files (product images)
│
└── tests/                        # Centralized tests
    ├── __init__.py
    ├── test_accounts.py
    ├── test_products.py
    ├── test_orders.py
    └── test_payments.py
```
