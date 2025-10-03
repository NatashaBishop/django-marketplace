
'''marketplace/
├── manage.py
├── requirements.txt
├── .env
│
├── marketplace/                # Project config
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── apps/
│   ├── accounts/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/accounts/
│   │       ├── login.html
│   │       └── register.html
│   │
│   ├── products/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/products/
│   │       ├── product_list.html
│   │       └── product_detail.html
│   │
│   ├── orders/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/orders/
│   │       ├── cart.html
│   │       └── checkout.html
│   │
│   └── payments/
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── templates/payments/
│           └── payment_success.html
│
└── static/
    └── css/'''
